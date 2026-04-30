# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        def dfs(root, m):
            if not root:
                return
            
            if root.val >= m:
                res.append(root)
            M = max(root.val, m)
            dfs(root.left, M)
            dfs(root.right, M)
        dfs(root, root.val)
        return len(res)