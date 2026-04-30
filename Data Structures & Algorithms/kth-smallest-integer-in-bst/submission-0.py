# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = 0
        res = 0
        def dfs(root):
            nonlocal seen, res
            if not root:
                return 0
            dfs(root.left)
            seen += 1
            if seen == k:
                res = root.val
            dfs(root.right)
            return seen
        dfs(root)
        return res
            
            