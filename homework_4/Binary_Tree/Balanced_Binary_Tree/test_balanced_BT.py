import unittest
from balanced_BT import is_balanced

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestBalancedBinaryTree(unittest.TestCase):
    def test_empty_tree(self):
        self.assertIs(is_balanced(None), True)

    def test_single_node(self):
        self.assertIs(is_balanced(Node(1)), True)

    def test_height_difference_one(self):
        root = Node(1)
        root.left = Node(2)
        self.assertIs(is_balanced(root), True)

    def test_left_subtree_too_tall(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertIs(is_balanced(root), False)

    def test_right_subtree_too_tall(self):
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        self.assertIs(is_balanced(root), False)

    def test_balanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertIs(is_balanced(root), True)

    def test_unbalanced_subtree_with_balanced_root(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(4)
        root.left.left.left = Node(6)
        root.right = Node(3)
        root.right.right = Node(5)
        self.assertIs(is_balanced(root), False)