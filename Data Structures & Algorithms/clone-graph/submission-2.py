"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}
        clones[node] = Node(node.val)
        visited = set()

        q = deque([node])
        visited.add(node)
        while q:
            curr = q.popleft()
            for nbr in curr.neighbors:
                if nbr not in clones:
                    clones[nbr] = Node(nbr.val)
                if nbr not in visited:
                    q.append(nbr)
                clones[curr].neighbors.append(clones[nbr])
                visited.add(nbr)

        return clones[node]
