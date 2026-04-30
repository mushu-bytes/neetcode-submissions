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
                    res.append("")
            q = level
        return ",".join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return
        flat_bt = data.split(',')
        ans = TreeNode(flat_bt[0])
        queue = collections.deque([ans])
        i = 1
        # when you pop a node, its children will be at i and i+1
        while queue:
            node = queue.pop()
            if i < len(flat_bt) and flat_bt[i]:
                node.left = TreeNode(int(flat_bt[i]))
                queue.appendleft(node.left)
            i += 1
            if i < len(flat_bt) and flat_bt[i]:
                node.right = TreeNode(int(flat_bt[i]))
                queue.appendleft(node.right)
            i += 1
        return ans



