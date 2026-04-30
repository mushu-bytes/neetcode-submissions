class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        How do we detect a disconnected graph?
        """
        
        adj = defaultdict(list)
        for h, t in edges:
            adj[h].append(t)
            adj[t].append(h)

        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False

            visited.add(curr)
            for nbr in adj[curr]:
                if nbr != prev and not dfs(nbr, curr):
                    return False

            return True
        
        if not dfs(0, None):
            return False
        return len(visited) == n
