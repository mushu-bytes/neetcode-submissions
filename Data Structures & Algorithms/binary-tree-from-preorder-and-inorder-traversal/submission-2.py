# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        root = preorder[0] 
        center = inorder.index(root)
        # length of left subtree
        leftLen = center
        # length of right subtree
        rightLen = len(inorder) - center - 1
        print(preorder[center + 1 + leftLen: ], inorder[center + 1:])
        
        rootNode = TreeNode(root)
        rootNode.left = self.buildTree(preorder[1: 1 + leftLen], inorder[:center])
        rootNode.right = self.buildTree(preorder[1 + leftLen: ], inorder[center + 1:])
        return rootNode
            
        


