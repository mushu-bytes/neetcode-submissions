"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(0)
        curr = newHead
        node_to_val = {None: None}
        val_to_newNode = {None: None}
        i = 0
        currHead = head
        
        while currHead:
            prev = curr
            curr = Node(currHead.val)
            prev.next = curr
            node_to_val[ currHead ] = i
            val_to_newNode[ i ] = curr
            currHead = currHead.next
            i += 1
        
        curr = newHead.next
        while curr:
            curr.random = val_to_newNode[ node_to_val[ head.random ] ]
            curr = curr.next
            head = head.next
        return newHead.next






