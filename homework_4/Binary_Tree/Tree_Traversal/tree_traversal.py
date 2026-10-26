class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        node = self.root
        while True:
            if value == node.value:
                return
            if value < node.value:
                child = node.left
            else:
                child = node.right
            if child is None:
                if value < node.value:
                    node.left = Node(value)
                else:
                    node.right = Node(value)
                return
            node = child

    def traverse(self, order):
        result = []

        def visit(node):
            if node is None:
                return
            for action in order:
                if action == "N":
                    result.append(node.value)
                elif action == "L":
                    visit(node.left)
                else:
                    visit(node.right)

        visit(self.root)
        return result

    def preorder(self):
        return self.traverse("NLR")

    def inorder(self):
        return self.traverse("LNR")

    def postorder(self):
        return self.traverse("LRN")

    def reverse_preorder(self):
        return self.traverse("NRL")

    def reverse_inorder(self):
        return self.traverse("RNL")

    def reverse_postorder(self):
        return self.traverse("RLN")