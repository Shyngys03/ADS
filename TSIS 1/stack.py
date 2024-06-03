class Stack: #LIFO
    
    def __init__(self) -> None:
        self.elements = []

    def push(self, n: int) -> None:
        self.elements.append(n)

    def pop(self) -> None:
        if len(self.elements) == 0:
            raise IndexError("Stack is empty")
        
        self.elements.pop()
    
    def top(self) -> None:
        if len(self.elements) == 0:
            raise IndexError("Stack is empty")
        
        return self.elements[-1]

    def size(self) -> int:
        return len(self.elements)
    
    def empty(self) -> bool:
        return self.elements == []
    
    def clear(self) -> None:
        self.elements.clear()
        # self.elements = []