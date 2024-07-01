class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
            
        self.table[index].append([key, value])

    def delete(self, key):
        index = self.hash_function(key)

        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return

    def search(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None


hash_table = HashTable()
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")
print(hash_table.search("key1"))  # Output: value1
print(hash_table.search("key4"))  # Output: None
hash_table.delete("key2")
print(hash_table.search("key2"))  # Output: None
print(hash_table.search("key3"))  # Output: value3
