from typing import Optional

class Node:
    def __init__(self, val: int = None) -> None:
        self.value = val
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def empty(self) -> bool:
        return self.head is None

    def insert_at_beginning(self, val: int) -> None:
        new_node = Node(val)

        if self.empty():
            self.tail = new_node
        else:
            self.head.prev = new_node

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, val: int) -> None:
        new_node = Node(val)

        if self.empty():
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        
        self.tail = new_node

    def delete_at_beginning(self) -> Optional[Node]:
        if self.empty():
            return None
        
        temp_link = self.head

        if self.head.next is None:
            self.tail = None
        else:
            self.head.next.prev = None
        self.head = self.head.next

        return temp_link
    
    def delete_at_end(self) -> Optional[Node]:
        if self.empty():
            return None
        
        temp_link = self.tail

        if self.head.next is None:
            self.head = None
        else:
            self.tail.prev.next = None
        self.tail = self.tail.prev

        return temp_link

    def display_forward(self):
        ptr = self.head
        result = []

        while ptr:
            result.append(ptr.value)
            ptr = ptr.next

        return result

    def display_backward(self):
        ptr = self.tail
        result = []

        while ptr:
            result.append(ptr.value)
            ptr = ptr.prev

        return result


dll = DoubleLinkedList()

dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.delete_at_beginning()
dll.delete_at_end()

print(dll.display_forward())
print(dll.display_backward())
