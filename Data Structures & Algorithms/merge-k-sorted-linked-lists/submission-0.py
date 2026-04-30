# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while True:
            min_index = 0
            min_val = float('inf')
            nones = 0
            for i in range(len(lists)):
                if lists[i] == None:
                    nones += 1
                    continue

                if lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index= i

            if nones == len(lists):
                break
            curr.next = ListNode(min_val)
            curr = curr.next
            lists[min_index] = lists[min_index].next
        return dummy.next
            






            