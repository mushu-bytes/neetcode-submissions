class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for cls, req in prerequisites:
            adj[cls].append(req)

        visited = set()
        res = []
        resSet = set()

        def dfs(i):
            if not adj[i]:
                if i not in resSet:
                    res.append(i)
                    resSet.add(i)
                return True
            if i in visited:
                return False

            visited.add(i)
            for nbr in adj[i]:
                if not dfs(nbr):
                    return False
            visited.remove(i)
            adj[i] = []
            if i not in resSet:
                res.append(i)
                resSet.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

        
