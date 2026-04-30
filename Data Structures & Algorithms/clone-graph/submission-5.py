"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        n2c = {node: Node(node.val)} # real: clone
        stack = [node]
        seen = set()
        seen.add(node)
        
        while stack:
            curr = stack.pop()
            for nbr in curr.neighbors:
                if nbr in n2c:
                    n2c[curr].neighbors.append(n2c[nbr])
                else:
                    n2c[nbr] = Node(nbr.val)
                    n2c[curr].neighbors.append(n2c[nbr])
                if nbr not in seen:
                    stack.append(nbr)
                    seen.add(nbr)

        return n2c[node]
