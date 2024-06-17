from typing import Optional

class Node:
    def __init__(self, val: int = None) -> None:
        self.value = val
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self, node: Node = None) -> None:
        self.root: Optional[Node] = None

    def insert(self, val: int) -> None:
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        parent = None
        
        while True:
            parent = current
            if val < parent.value:
                current = current.left_child

                if current is None:
                    parent.left_child = new_node
                    return
                
            else:
                current = current.right_child

                if current is None:
                    parent.right_child = new_node
                    return
                
    def in_order_traversal(self, node: Optional[Node]) -> None:
        if node:
            self.in_order_traversal(node.left_child)
            print(node.value)
            self.in_order_traversal(node.right_child)

    def pre_order_traversal(self, node: Optional[Node]) -> None:
        if node:
            print(node.value)
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)

    def post_order_traversal(self, node: Optional[Node]) -> None:
        if node:
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)
            print(node.value)

    def search(self, key: int, node: Optional[Node]) -> bool:
        if node is None:
            return False
        
        if node.value == key:
            return True

        if key < node.value:
            return self.search(key, node.left_child)

        if key > node.value:
            return self.search(key, node.right_child)

        return False

a = [27, 14, 35, 10, 19, 31, 42]

bst = BST()
for i in a:
    bst.insert(i)

bst.in_order_traversal(bst.root)

print(bst.search(42, bst.root))