# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        prev = curr
        while True:
            curr = curr.next
            for i in range(k - 1):
                if not curr:
                    break
                curr = curr.next
            if not curr:
                print("premature end")
                break
            end = curr
            curr = curr.next
            end.next = None

            newPrev = prev.next
            newHead = self.reverse(prev.next, curr)
            prev.next = newHead
            prev = newPrev
            curr = prev
            
        return dummy.next
    # curr and prev are the start and end of the list
    def reverse(self, curr, prev):
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        return prev


