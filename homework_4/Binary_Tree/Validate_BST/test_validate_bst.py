import unittest

from Validate_BST import is_valid_bst


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestValidateBST(unittest.TestCase):
    def test_empty_tree(self):
        self.assertIs(is_valid_bst(None), True)

    def test_single_node(self):
        self.assertIs(is_valid_bst(Node(2)), True)

    def test_valid_tree(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.left = Node(2)
        root.left.right = Node(7)
        root.right.left = Node(12)
        root.right.right = Node(20)
        self.assertIs(is_valid_bst(root), True)

    def test_violation_in_right_subtree(self):
        root = Node(10)
        root.right = Node(15)
        root.right.left = Node(6)
        self.assertIs(is_valid_bst(root), False)

    def test_violation_in_left_subtree(self):
        root = Node(10)
        root.left = Node(5)
        root.left.right = Node(12)
        self.assertIs(is_valid_bst(root), False)

    def test_duplicate_on_left(self):
        root = Node(10)
        root.left = Node(10)
        self.assertIs(is_valid_bst(root), False)

    def test_duplicate_on_right(self):
        root = Node(10)
        root.right = Node(10)
        self.assertIs(is_valid_bst(root), False)

    def test_negative_values_and_zero(self):
        root = Node(0)
        root.left = Node(-5)
        root.left.left = Node(-10)
        root.left.right = Node(-2)
        root.right = Node(5)
        self.assertIs(is_valid_bst(root), True)

    def test_zero_as_upper_bound(self):
        root = Node(0)
        root.left = Node(-5)
        root.left.right = Node(1)
        self.assertIs(is_valid_bst(root), False)

    def test_zero_as_lower_bound(self):
        root = Node(0)
        root.right = Node(5)
        root.right.left = Node(-1)
        self.assertIs(is_valid_bst(root), False)

