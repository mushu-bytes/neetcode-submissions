# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        inTraversal = []
        preTraversal = []
        def dfs(root):
            if not root:
                return None
            val = str(root.val)

            preTraversal.append(val)
            preTraversal.append("|")
            dfs(root.left)
            inTraversal.append(val)
            inTraversal.append("|")
            dfs(root.right)
            
        dfs(root)
        return "".join(inTraversal + ["&"] + preTraversal) 
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        inorder, preorder = data.split("&")
        inorder = inorder.split("|")[:-1]
        preorder = preorder.split("|")[:-1]
        print(inorder, preorder)
        
        def dfs(inorder, preorder):
            if not inorder and not preorder:
                return None
            center = inorder.index(preorder[0])
            curr = TreeNode(int(preorder[0]))
            curr.left = dfs(inorder[:center], preorder[1 : 1 + center])
            curr.right = dfs(inorder[center + 1:], preorder[1 + center:])
            return curr

        return dfs(inorder, preorder)

