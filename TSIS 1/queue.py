class Queue: #FIFO
    
    def __init__(self) -> None:
        self.elements = []

    def push(self, n: int) -> None:
        self.elements.append(n)

    def pop(self) -> None:
        if self.empty():
            raise IndexError("Queue is empty")
        
        self.elements.pop(0)
    
    def front(self) -> int:
        if self.empty():
            raise IndexError("Queue is empty")
        
        return self.elements[0]

    def size(self) -> int:
        return len(self.elements)
    
    def empty(self) -> bool:
        return self.elements == []
    
    def clear(self) -> None:
        self.elements.clear()
        # self.elements = []