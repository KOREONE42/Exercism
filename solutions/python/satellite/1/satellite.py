def tree_from_traversals(preorder, inorder):
    # Check that both traversals are of the same length.
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    
    # Check that both traversals contain unique items.
    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")
    
    # Check that both traversals have exactly the same elements.
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    
    # Base case: if there's no element, return an empty tree.
    if not preorder:
        return {}

    # The first element of pre-order is always the root.
    root = preorder[0]
    
    # Find the index of the root in in-order list.
    # This will divide the in-order list into left and right subtrees.
    try:
        root_index = inorder.index(root)
    except ValueError:
        # This should not happen given previous checks.
        raise ValueError("traversals must have the same elements")
    
    # Split the in-order traversal for left and right subtrees.
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]
    
    # The number of elements in the left subtree in in-order
    # determines how many elements belong to the left subtree in pre-order.
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    
    # Recursively build the left and right subtrees.
    left_tree = tree_from_traversals(left_preorder, left_inorder)
    right_tree = tree_from_traversals(right_preorder, right_inorder)
    
    # Construct and return the dictionary representing the tree.
    return {"v": root, "l": left_tree, "r": right_tree}
