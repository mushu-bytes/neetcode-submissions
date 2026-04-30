class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for cls, req in prerequisites:
            adj[cls].append(req)

        visited = set()
        def dfs(i):
            if not adj[i]:
                return True
            if i in visited:
                return False
            
            visited.add(i)
            for req in adj[i]:
                if not dfs(req):
                    return False
            visited.remove(i)
            adj[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        


"""
The question is: how do we determine a cycle?

"""





