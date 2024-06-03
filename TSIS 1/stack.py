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


my_stack = Stack()

my_stack.push(1) # now stack = [1]
my_stack.push(2) # now stack = [1, 2]

print(my_stack.top()) # will return 2, because last element is 2
print(my_stack.size()) # will return 2, because there are 2 elements

my_stack.pop() # now stack = [1]
print(my_stack.empty()) # return False, because stack has 1 element

my_stack.push(12) # now stack = [1, 12]

my_stack.clear() # now stack = []

# Now stack is empty and if you try to use top() or pop() methods, it will return IndexError

my_stack.top()