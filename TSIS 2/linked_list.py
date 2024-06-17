from typing import Optional

class Node:
    def __init__(self, val: int = None) -> None:
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, node: Node = None) -> None:
        self.head: Optional[Node] = None

    def display(self) -> None:
        current = self.head
        
        print("[", end=" ")
        
        while current:
            print(current.value, end=" ")
            current = current.next

        print("]")

    def insert_at_beginning(self, n: int) -> None:
        new_node = Node(n)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, n: int) -> None:
        if self.head is None:
            self.head = Node(n)
            return
        
        current = self.head

        while current.next:
            current = current.next
            
        current.next = Node(n)

    def delete_at_beginning(self) -> None:
        if self.head is None: 
            return
        if self.head.next is None:
            self.head = None

        self.head = self.head.next


    def delete_at_end(self) -> None:
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None

    def search(self, key: int) -> bool:
        current = self.head

        while current.next:
            if current.value == key:
                return True
            
        return False