from json import dumps

class Tree:
    def __init__(self, label, children=None):
        """
        Initialize a Tree node.

        Args:
            label (str): The label for this node.
            children (list[Tree], optional): List of child Tree nodes.
        """
        self.label = label
        self.children = children if children else []

    def __dict__(self):
        """
        Represent the tree as a dictionary (used for equality and display).

        Returns:
            dict: Tree represented as a nested dictionary.
        """
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        """
        Convert the tree to a JSON-formatted string.

        Args:
            indent (int, optional): Indentation for pretty-printing.

        Returns:
            str: String representation of the tree.
        """
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        """
        Less-than comparison based on node labels (for sorting).

        Args:
            other (Tree): Another Tree node.

        Returns:
            bool: True if self is less than other.
        """
        return self.label < other.label

    def __eq__(self, other):
        """
        Check structural and label equality of trees.

        Args:
            other (Tree): Another Tree node.

        Returns:
            bool: True if trees are equal.
        """
        return self.__dict__() == other.__dict__()

    def _find_path(self, target, path=None):
        """
        Recursively find a path from the current node to a target node.

        Args:
            target (str): Label of the target node.
            path (list[Tree], optional): Accumulated path for recursion.

        Returns:
            list[Tree] or None: Path to the target node, or None if not found.
        """
        path = path or []

        if self.label == target:
            return path + [self]

        for child in self.children:
            result = child._find_path(target, path + [self])
            if result:
                return result

        return None

    def from_pov(self, from_node):
        """
        Reorient the tree so that from_node becomes the new root.

        Args:
            from_node (str): The label of the new root node.

        Returns:
            Tree: A new tree rooted at from_node.

        Raises:
            ValueError: If from_node is not found in the tree.
        """
        path = self._find_path(from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")

        new_root = path[-1]

        # Reverse the parent-child relationship along the path
        for i in range(len(path) - 2, -1, -1):
            parent = path[i]
            child = path[i + 1]

            parent.children.remove(child)
            child.children.append(parent)

        return new_root

    def path_to(self, from_node, to_node):
        """
        Find the path from from_node to to_node.

        Args:
            from_node (str): The starting node label.
            to_node (str): The destination node label.

        Returns:
            list[str]: List of labels from from_node to to_node.

        Raises:
            ValueError: If from_node is not in the tree.
            ValueError: If to_node is not reachable from from_node.
        """
        try:
            root_from = self.from_pov(from_node)
        except ValueError:
            raise ValueError("Tree could not be reoriented")

        path = root_from._find_path(to_node)
        if not path:
            raise ValueError("No path found")

        return [node.label for node in path]
