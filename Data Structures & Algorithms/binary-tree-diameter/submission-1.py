# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0, 0
            ldiam, left = dfs(root.left)
            rdiam, right = dfs(root.right)
            res = max(ldiam, rdiam, left + right)
            return res, 1 + max(left, right)

        res, height = dfs(root)
        return res
        