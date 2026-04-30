# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(head):
            if not head:
                return None
            if not head.left and not head.right:
                return head
                
            head.left, head.right = invert(head.right), invert(head.left)
            return head
        return invert(root)