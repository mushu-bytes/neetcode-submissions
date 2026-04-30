# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        for i in range(n):
            curr = curr.next

        left = dummy
        while curr and curr.next:
            left = left.next
            curr = curr.next

        left.next = left.next.next
        
        return dummy.next