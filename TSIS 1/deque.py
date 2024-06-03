class Deque:
    def __init__(self) -> None:
        self.elements = []

    def empty(self) -> bool:
        return self.elements == []

    def push_back(self, n: int) -> None:
        self.elements.append()

    def push_front(self, n: int) -> None:
        self.elements.insert(0, n)

    def pop_back(self) -> None:
        if self.empty():
            raise IndexError("Deque is empty")
        
        self.elements.pop()

    def pop_front(self) -> None:
        if self.empty():
            raise IndexError("Deque is empty")
        
        self.elements.pop(0)

    def front(self) -> int:
        if self.empty():
            raise IndexError("Deque is empty")

        return self.elements[0]
    
    def back(self) -> int:
        if self.empty():
            raise IndexError("Deque is empty")
        
        return self.elements[-1]
    
    def size(self) -> int:
        return len(self.elements)
    
    def clear(self) -> None:
        self.elements.clear()
        # self.elements = []