# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) != 1:
            newList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                newList.append(self.merge(l1, l2))
            lists = newList
        return lists[0]


    def merge(self, list1, list2):
        cur1, cur2 = list1, list2
        dummy = ListNode()
        new = dummy
        while cur1 and cur2:
            if cur1.val < cur2.val:
                new.next = ListNode(cur1.val)
                new = new.next
                cur1 = cur1.next
            else:
                new.next = ListNode(cur2.val)
                new = new.next
                cur2 = cur2.next
        new.next = cur1 or cur2
        return dummy.next
        
            






            