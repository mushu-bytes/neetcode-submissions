# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return True, 0
            balancedL, left = dfs(root.left)
            balancedR, right = dfs(root.right)
            balanced = balancedL and balancedR

            if abs(left - right) > 1:
                balanced = False
            return balanced, 1 + max(left, right)

        balanced, height = dfs(root)
        return balanced
