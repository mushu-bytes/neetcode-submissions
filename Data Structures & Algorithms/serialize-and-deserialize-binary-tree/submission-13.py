# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        q = [root]
        res = []
        while q:
            level = []
            for i in range(len(q)):
                curr = q.pop(0)
                if curr:
                    res.append(str(curr.val))
                    level.append(curr.left)
                    level.append(curr.right)
                else:
                    res.append("N")
            q = level
        return ",".join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        if not data or data[0] == "N":
            return
        data = data.split(",")
        root = TreeNode(int(data[0]))
        q = [root]
        i = 1
        while q:
            node = q.pop(0)
            if i < len(data) and data[i] != "N":
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i += 1
            if i < len(data) and data[i] != "N":
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i += 1

        return root




