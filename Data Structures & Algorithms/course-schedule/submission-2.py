class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for cls, req in prerequisites:
            adj[cls].append(req)

        def dfs(i, visited):
            if not adj[i]:
                return True
            if i in visited:
                return False

            visited.add(i)
            for req in adj[i]:
                if not dfs(req, visited):
                    return False
            
            adj[i] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True


"""
The question is: how do we determine a cycle?

"""





