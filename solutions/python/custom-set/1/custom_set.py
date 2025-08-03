class CustomSet:
    def __init__(self, elements=None):
        # Initialize with unique elements preserving order
        if elements is None:
            elements = []
        self._elements = []
        for e in elements:
            if e not in self._elements:
                self._elements.append(e)

    def isempty(self):
        # Return True if set has no elements
        return len(self._elements) == 0

    def __contains__(self, element):
        # Support "in" operator
        return element in self._elements

    def issubset(self, other):
        # Return True if every element in self is in other
        for e in self._elements:
            if e not in other:
                return False
        return True

    def isdisjoint(self, other):
        # Return True if no element in self is in other
        for e in self._elements:
            if e in other:
                return False
        return True

    def __eq__(self, other):
        # Two sets are equal if they contain the same elements
        if not isinstance(other, CustomSet):
            return False
        return self.issubset(other) and other.issubset(self)

    def add(self, element):
        # Add element if not already present
        if element not in self._elements:
            self._elements.append(element)

    def intersection(self, other):
        # Return a new CustomSet of elements common to both
        common = [e for e in self._elements if e in other]
        return CustomSet(common)

    def __sub__(self, other):
        # Return a new CustomSet of elements in self but not in other
        diff = [e for e in self._elements if e not in other]
        return CustomSet(diff)

    def __add__(self, other):
        # Return the union of two sets
        new_elems = self._elements.copy()
        # Add elements from other that are not already in new_elems
        for e in other._elements:
            if e not in new_elems:
                new_elems.append(e)
        return CustomSet(new_elems)
