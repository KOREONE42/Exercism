class InputCell:
    def __init__(self, initial_value):
        # Current value and dependents (compute cells that depend on this cell)
        self._value = initial_value
        self.dependents = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # Only trigger propagation if value actually changes
        if self._value == new_value:
            return
        self._value = new_value
        # Propagate changes to dependent compute cells
        self._propagate()

    def _propagate(self):
        # Collect all affected compute cells via BFS
        affected = set()
        queue = list(self.dependents)
        while queue:
            cell = queue.pop(0)
            if cell not in affected:
                affected.add(cell)
                queue.extend(cell.dependents)

        # Topological sort of affected compute cells
        # Compute indegrees: number of dependencies within affected
        indegree = {}
        for cell in affected:
            indegree[cell] = sum(
                1 for inp in cell.inputs
                if isinstance(inp, ComputeCell) and inp in affected
            )
        # Start with cells that depend only on inputs or unaffected cells
        order = []
        zero = [cell for cell, deg in indegree.items() if deg == 0]
        while zero:
            cell = zero.pop(0)
            order.append(cell)
            for dep in cell.dependents:
                if dep in indegree:
                    indegree[dep] -= 1
                    if indegree[dep] == 0:
                        zero.append(dep)

        # Recompute in order, tracking which changed
        changed = []
        for cell in order:
            new_value = cell.compute_fn([inp.value for inp in cell.inputs])
            if new_value != cell._value:
                cell._value = new_value
                changed.append(cell)

        # Fire callbacks for changed compute cells
        for cell in changed:
            for callback in list(cell.callbacks):
                callback(cell.value)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        # Dependencies and dependents
        self.inputs = inputs
        self.compute_fn = compute_function
        self.dependents = []
        # Registered callbacks
        self.callbacks = []
        # Register this cell as dependent on inputs
        for inp in self.inputs:
            inp.dependents.append(self)
        # Compute initial value
        self._value = self.compute_fn([inp.value for inp in self.inputs])

    @property
    def value(self):
        return self._value

    def add_callback(self, callback):
        # Register a callback to be notified when value changes
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def remove_callback(self, callback):
        # Unregister a previously registered callback
        try:
            self.callbacks.remove(callback)
        except ValueError:
            pass
