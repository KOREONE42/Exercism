from json import dumps

class Tree:
    def __init__(self, label, children=None):
        """
        Initialize a Tree node.

        :param label: The label of the current node.
        :param children: A list of child Tree nodes.
        """
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        """
        Represent the tree as a dictionary (used for comparisons and printing).

        :return: Dictionary with the node label as key and list of children as value.
        """
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        """
        Convert the tree to a pretty-printed JSON string.

        :param indent: Indentation level for pretty-printing.
        :return: JSON string representation of the tree.
        """
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        """
        Compare nodes based on their labels for sorting purposes.

        :param other: Another Tree node.
        :return: True if self's label is less than other's label.
        """
        return self.label < other.label

    def __eq__(self, other):
        """
        Check equality between two trees based on structure and labels.

        :param other: Another Tree node.
        :return: True if both trees are structurally equal.
        """
        return self.__dict__() == other.__dict__()

    def _find_path(self, target, path=None):
        """
        Internal helper to find a path from current node to the target node.

        :param target: The label of the target node.
        :param path: Accumulator list to build the path during recursion.
        :return: List of Tree nodes from current node to target, or None if not found.
        """
        if path is None:
            path = []
        if self.label == target:
            return path + [self]

        for child in self.children:
            result = child._find_path(target, path + [self])
            if result:
                return result

        return None

    def from_pov(self, from_node):
        """
        Reorient the tree to have the specified node as the new root.

        :param from_node: The label of the node to become the new root.
        :return: A new Tree with from_node as the root.
        :raises ValueError: If from_node does not exist in the tree.
        """
        path = self._find_path(from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")

        # Start at the new root node
        new_root = path[-1]

        # Reverse the parent-child relationship along the path
        for i in range(len(path) - 2, -1, -1):
            parent = path[i]
            child = path[i + 1]

            # Remove the forward link and create a backward link
            parent.children.remove(child)
            child.children.append(parent)

        return new_root

    def path_to(self, from_node, to_node):
        """
        Find the path from one node to another.

        :param from_node: The starting node's label.
        :param to_node: The destination node's label.
        :return: List of labels representing the path from from_node to to_node.
        :raises ValueError: If from_node is not in the tree ("Tree could not be reoriented")
                            or if to_node is not found from from_node ("No path found").
        """
        # Reorient tree so from_node becomes the root
        root_from = self.from_pov(from_node)

        # Now find path from root to to_node
        path = root_from._find_path(to_node)
        if not path:
            raise ValueError("No path found")

        return [node.label for node in path]
