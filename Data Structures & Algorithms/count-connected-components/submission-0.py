class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # form adj list
        adj = defaultdict(list)
        visited = set()
        res = 0
        for h, t in edges:
            adj[h].append(t)
            adj[t].append(h)
        
        def dfs(curr, prev):
            if curr in visited:
                return
            
            visited.add(curr)
            for nbr in adj[curr]:
                if nbr != prev:
                    dfs(nbr, curr)
            return

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1
        return res
