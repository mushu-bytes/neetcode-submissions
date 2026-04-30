class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.cap = 10000
        self.arr = [ListNode(-1, -1) for _ in range(self.cap)]

    def put(self, key: int, value: int) -> None:
        chain = self.arr[key % self.cap] # listNode
        while chain:
            # if key already exists
            if chain.key == key:
                chain.value = value
                return
            # if we reached the end
            if not chain.next:
                chain.next = ListNode(key, value)
                return

            chain = chain.next


    def get(self, key: int) -> int:
        chain = self.arr[key % self.cap] # listNode
        while chain:
            if chain.key == key:
                return chain.value
            
            chain = chain.next
        return -1
        
    def remove(self, key: int) -> None:
        chain = self.arr[key % self.cap] # listNode
        while chain and chain.next:
            if chain.next.key == key:
                chain.next = chain.next.next
            
            chain = chain.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)