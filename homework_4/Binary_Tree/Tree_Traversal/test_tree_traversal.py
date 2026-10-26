import unittest
from tree_traversal import BST


class TestBST(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            self.tree.insert(value)

    def test_preorder(self):
        self.assertEqual(
            self.tree.preorder(),
            [8, 3, 1, 6, 4, 7, 10, 14, 13],
        )

    def test_inorder(self):
        self.assertEqual(
            self.tree.inorder(),
            [1, 3, 4, 6, 7, 8, 10, 13, 14],
        )

    def test_postorder(self):
        self.assertEqual(
            self.tree.postorder(),
            [1, 4, 7, 6, 3, 13, 14, 10, 8],
        )

    def test_reverse_preorder(self):
        self.assertEqual(
            self.tree.reverse_preorder(),
            [8, 10, 14, 13, 3, 6, 7, 4, 1],
        )

    def test_reverse_inorder(self):
        self.assertEqual(
            self.tree.reverse_inorder(),
            [14, 13, 10, 8, 7, 6, 4, 3, 1],
        )

    def test_reverse_postorder(self):
        self.assertEqual(
            self.tree.reverse_postorder(),
            [13, 14, 10, 7, 4, 6, 1, 3, 8],
        )

def test_empty_tree(self):
    tree = BST()
    self.assertEqual(tree.preorder(), [])
    self.assertEqual(tree.inorder(), [])
    self.assertEqual(tree.postorder(), [])
    self.assertEqual(tree.reverse_preorder(), [])
    self.assertEqual(tree.reverse_inorder(), [])
    self.assertEqual(tree.reverse_postorder(), [])

def test_single_node(self):
    tree = BST()
    tree.insert(2)
    self.assertEqual(tree.preorder(), [2])
    self.assertEqual(tree.inorder(), [2])
    self.assertEqual(tree.postorder(), [2])
    self.assertEqual(tree.reverse_preorder(), [2])
    self.assertEqual(tree.reverse_inorder(), [2])
    self.assertEqual(tree.reverse_postorder(), [2])

def test_duplicates_are_ignored(self):
    before = self.tree.inorder()
    self.tree.insert(8)
    self.tree.insert(3)
    self.tree.insert(13)
    self.assertEqual(self.tree.inorder(), before)

def test_negative_values_and_zero(self):
    tree = BST()
    for value in [0, -5, 5, -10, -2]:
        tree.insert(value)
    self.assertEqual(tree.inorder(), [-10, -5, -2, 0, 5])

def test_right_skewed_tree(self):
    tree = BST()
    for value in [1, 2, 3, 4]:
        tree.insert(value)
    self.assertEqual(tree.preorder(), [1, 2, 3, 4])
    self.assertEqual(tree.inorder(), [1, 2, 3, 4])
    self.assertEqual(tree.postorder(), [4, 3, 2, 1])
    self.assertEqual(tree.reverse_preorder(), [1, 2, 3, 4])
    self.assertEqual(tree.reverse_inorder(), [4, 3, 2, 1])
    self.assertEqual(tree.reverse_postorder(), [4, 3, 2, 1])

def test_left_skewed_tree(self):
    tree = BST()
    for value in [4, 3, 2, 1]:
        tree.insert(value)
    self.assertEqual(tree.preorder(), [4, 3, 2, 1])
    self.assertEqual(tree.inorder(), [1, 2, 3, 4])
    self.assertEqual(tree.postorder(), [1, 2, 3, 4])
    self.assertEqual(tree.reverse_preorder(), [4, 3, 2, 1])
    self.assertEqual(tree.reverse_inorder(), [4, 3, 2, 1])
    self.assertEqual(tree.reverse_postorder(), [1, 2, 3, 4])
