import unittest
from AVL import AVL


class TestAVL(unittest.TestCase):
    def check_tree(self, tree, expected):
        values = []
        def check(node):
            if node is None:
                return 0
            left = check(node.left)
            values.append(node.value)
            right = check(node.right)
            self.assertLessEqual(abs(left - right), 1)
            self.assertEqual(node.height, 1 + max(left, right))
            return 1 + max(left, right)
        check(tree.root)
        self.assertEqual(values, sorted(expected))

    def test_empty_tree(self):
        tree = AVL()
        self.assertFalse(tree.search(10))
        tree.delete(10)
        self.check_tree(tree, [])

    def test_insert_and_search(self):
        tree = AVL()
        for value in [20, 10, 30, 10]:
            tree.insert(value)
        self.check_tree(tree, [10, 20, 30])  
        for value in [10, 20, 30]:
            self.assertTrue(tree.search(value))
        self.assertFalse(tree.search(99))

    def test_rotations(self):
        for values in [[30, 20, 10], [10, 20, 30], [30, 10, 20], [10, 30, 20]]:
            with self.subTest(values=values):
                tree = AVL()
                for value in values:
                    tree.insert(value)
                self.assertEqual(tree.root.value, 20)
                self.check_tree(tree, [10, 20, 30])

    def test_delete(self):
        tree = AVL()
        expected = {20, 10, 30, 25}
        for value in sorted(expected):
            tree.insert(value)
        for value in [99, 30, 20, 10, 25]:
            tree.delete(value)
            expected.discard(value)
            self.assertFalse(tree.search(value))
            self.check_tree(tree, expected)
        self.assertIsNone(tree.root)

    def test_balance_after_delete(self):
        tree = AVL()
        for value in [30, 20, 40, 10, 25]:
            tree.insert(value)
        tree.delete(40)
        self.assertEqual(tree.root.value, 20)
        self.check_tree(tree, [10, 20, 25, 30])
