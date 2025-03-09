class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return

        self.table[index].append([key, value])

    def delete(self, key):
        index = self._hash(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return True

        return False

    def search(self, key):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def __str__(self):
        return str(self.table)


hash_table = HashTable()

hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)
hash_table.insert("grape", 4)

print("Search 'banana':", hash_table.search("banana"))

hash_table.delete("orange")

print("Hash Table:", hash_table)

