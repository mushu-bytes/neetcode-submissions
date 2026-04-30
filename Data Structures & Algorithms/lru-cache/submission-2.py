class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key: Node
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # given a pointer to node A, remove node A
    def remove(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

    # given a pointer to node A, insert node A at right end of list
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)

        print(self.left.next.value, self.right.prev.value, self.cap, len(self.cache))

        
