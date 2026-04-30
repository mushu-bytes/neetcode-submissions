# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val > curr2.val:
                head.next = curr2
                curr2 = curr2.next
                head = head.next
            else:
                head.next = curr1
                curr1 = curr1.next
                head = head.next
        
        if curr1:
            head.next = curr1
        else:
            head.next = curr2
        return dummy.next
                

