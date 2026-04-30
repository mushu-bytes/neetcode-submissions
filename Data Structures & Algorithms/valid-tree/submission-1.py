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
        cycle = set()

        def dfs(curr, prev):
            if curr in cycle:
                return False

            visited.add(curr)
            cycle.add(curr)
            for nbr in adj[curr]:
                if nbr != prev and not dfs(nbr, curr):
                    return False

            cycle.remove(curr)
            return True

        #for i in range(n):
        #    if i not in visited and not dfs(i, None):
        #        return False
        
        if not dfs(0, None):
            return False
        return len(visited) == n
