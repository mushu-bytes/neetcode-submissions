# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the back half
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the back half
        curr = None
        while slow:
            nxt = slow.next
            slow.next = curr
            curr = slow
            slow = nxt
        
        # splice the lists together
        while head and curr:
            nxt = head.next
            next2 = curr.next

            head.next = curr
            curr.next = nxt
            
            head = nxt
            curr = next2
        





