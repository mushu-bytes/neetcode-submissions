class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyHashSet:

    def __init__(self):
        self.cap = 10000
        self.arr = [ListNode(-1) for _ in range(self.cap)]

    def add(self, key: int) -> None:
        hashcode = key % self.cap
        curr = self.arr[hashcode] # curr is a ListNode
        while curr.next:
            if curr.next.data == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        hashcode = key % self.cap
        curr = self.arr[hashcode]

        while curr and curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
            curr = curr.next

    def contains(self, key: int) -> bool:
        hashcode = key % self.cap
        curr = self.arr[hashcode]
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)