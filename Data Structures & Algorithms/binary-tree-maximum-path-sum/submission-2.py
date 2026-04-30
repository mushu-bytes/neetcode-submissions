# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> (int, int):
            if not root:
                return float('-inf'), float('-inf')
            
            lTreeSum, lRootSum = dfs(root.left)
            rTreeSum, rRootSum = dfs(root.right)

            maxSum = max(lTreeSum,
                        rTreeSum,
                        root.val + lRootSum,
                        root.val + rRootSum,
                        root.val + lRootSum + rRootSum,
                        root.val )
            maxCurrSum = max(root.val + lRootSum,
                             root.val + rRootSum,
                             root.val)
            return maxSum, maxCurrSum
        return max(dfs(root))
