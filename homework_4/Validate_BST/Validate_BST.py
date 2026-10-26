def is_valid_bst(root):
    
    def check(node, lower, upper):
        if node is None:
            return True
        if lower is not None and node.value <= lower:
            return False
        if upper is not None and node.value >= upper:
            return False
        return (
            check(node.left, lower, node.value)
            and check(node.right, node.value, upper)
        )

    return check(root, None, None)