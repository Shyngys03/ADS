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


my_queue = Queue()

my_queue.push(1) # now queue = [1]
my_queue.push(2) # now queue = [1, 2]

print(my_queue.front()) # will return 1, because first element is 1
print(my_queue.size()) # will return 2, because there are 2 elements

my_queue.pop() # now queue = [2]
print(my_queue.empty()) # return False, because stack has 1 element

my_queue.push(12) # now queue = [2, 12]

my_queue.clear() # now queue = []

# Now queue is empty and if you try to use top() or pop() methods, it will return IndexError

my_queue.front()