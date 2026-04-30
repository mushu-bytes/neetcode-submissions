# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        res = []

        while q:
            next_level = []
            for i in range(len(q)):
                if q[i].left:
                    next_level.append(q[i].left)
                if q[i].right:
                    next_level.append(q[i].right)
            res.append(q[i].val)
            q = next_level
        return res
