# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, m):
            if not root:
                return 0
            res = 0
            if root.val >= m:
                res += 1
            M = max(root.val, m)
            res += dfs(root.left, M)
            res += dfs(root.right, M)
            return res
        
        return dfs(root, root.val)