class Zipper:
    def __init__(self, tree, ctx):
        # tree is a dict {'value': v, 'left': subtree or None, 'right': subtree or None}
        # ctx is a breadcrumb: (side, parent_value, sibling_subtree, parent_ctx) or None at root
        self._tree = tree
        self._ctx = ctx

    @staticmethod
    def from_tree(tree):
        """Initialize a zipper focused on the root of the given tree."""
        return Zipper(tree, None)

    def value(self):
        """Return the value at the focus node."""
        return self._tree['value']

    def set_value(self, value):
        """Set the focus node's value to `value`, returning a new zipper."""
        new_tree = {
            'value': value,
            'left': self._tree['left'],
            'right': self._tree['right']
        }
        return Zipper(new_tree, self._ctx)

    def left(self):
        """Move focus to the left child. Return None if no left child."""
        left = self._tree['left']
        if left is None:
            return None
        # store a breadcrumb: we came from left, sibling is right
        breadcrumb = ('left', self._tree['value'], self._tree['right'], self._ctx)
        return Zipper(left, breadcrumb)

    def right(self):
        """Move focus to the right child. Return None if no right child."""
        right = self._tree['right']
        if right is None:
            return None
        # store a breadcrumb: we came from right, sibling is left
        breadcrumb = ('right', self._tree['value'], self._tree['left'], self._ctx)
        return Zipper(right, breadcrumb)

    def up(self):
        """Move focus to the parent node. Return None if at root."""
        if self._ctx is None:
            return None
        side, parent_value, sibling, parent_ctx = self._ctx
        # reconstruct the parent node using current focus and the stored sibling
        if side == 'left':
            tree = {
                'value': parent_value,
                'left': self._tree,
                'right': sibling
            }
        else:
            tree = {
                'value': parent_value,
                'left': sibling,
                'right': self._tree
            }
        return Zipper(tree, parent_ctx)

    def set_left(self, subtree):
        """Replace the left subtree of the focus node with `subtree`. Return a new zipper."""
        new_tree = {
            'value': self._tree['value'],
            'left': subtree,
            'right': self._tree['right']
        }
        return Zipper(new_tree, self._ctx)

    def set_right(self, subtree):
        """Replace the right subtree of the focus node with `subtree`. Return a new zipper."""
        new_tree = {
            'value': self._tree['value'],
            'left': self._tree['left'],
            'right': subtree
        }
        return Zipper(new_tree, self._ctx)

    def to_tree(self):
        """Return the complete tree by walking up to the root."""
        z = self
        while z._ctx is not None:
            z = z.up()
        return z._tree
