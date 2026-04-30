class MyHashSet:

    def __init__(self):
        self.cap = 10000
        self.arr = [[] for _ in range(self.cap)]

    def add(self, key: int) -> None:
        hashcode = key % self.cap
        if key not in self.arr[hashcode]:
            self.arr[hashcode].append(key)

    def remove(self, key: int) -> None:
        hashcode = key % self.cap
        if key in self.arr[hashcode]:
            self.arr[hashcode].remove(key)

    def contains(self, key: int) -> bool:
        hashcode = key % self.cap
        return key in self.arr[hashcode]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)