class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def in_order_traversal(self):
        nodes = []
        self._in_order_traversal(self.root, nodes)
        
        return nodes

    def _in_order_traversal(self, current_node, nodes):
        if current_node is not None:
            self._in_order_traversal(current_node.left, nodes)
            nodes.append(current_node.value)
            self._in_order_traversal(current_node.right, nodes)


# Example usage
binary_tree = BinaryTree()

# Insert nodes into the binary tree
binary_tree.insert(10)
binary_tree.insert(5)
binary_tree.insert(15)
binary_tree.insert(2)
binary_tree.insert(7)
binary_tree.insert(12)
binary_tree.insert(20)

# Perform an in-order traversal and print the result
print(binary_tree.in_order_traversal())  # Output: [2, 5, 7, 10, 12, 15, 20]
