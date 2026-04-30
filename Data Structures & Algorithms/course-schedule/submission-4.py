class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for cls, pre in prerequisites:
            adj[cls].append(pre)

        valid = set()
        seen = set()
        def dfs(i):
            if not adj[i]:
                return True
            if i in seen:
                return False

            seen.add(i)
            for req in adj[i]:
                if not dfs(req):
                    return False
            seen.remove(i)
            adj[i] = []
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        


"""
The question is: how do we determine a cycle?

"""





