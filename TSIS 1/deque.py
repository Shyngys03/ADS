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
   

deque = Deque()

deque.push_back(1) # now deque = [1]
deque.push_front(2) # now deque = [2, 1]
deque.push_back(3) # now deque = [2, 1, 3]
deque.push_front(4) # now deque = [4, 2, 1, 3]

deque.pop_back() # now deque = [4, 2, 1]
deque.pop_front() # now deque = [2, 1]
deque.pop_back() # now deque = [2]

deque.push_front(8) # now deque = [8, 2]

print(deque.back()) # will return 2
print(deque.front()) # will return 8

print(deque.size()) # will return 2, because there are 2 elements

deque.clear() # now deque = []

# Now deque is empty and if you try to use pop_front(), pop_back(), front(), back() methods, it will return IndexError

deque.back()