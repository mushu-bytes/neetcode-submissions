class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Same problem as course schedule 2, except we now have to
        output a valid order of courses. 
        If there are many valid answers: return any of them
        What is a valid ordering of courses; just so that the
        prereqs are finished before taking a course
        So the easiest way to do this, is to append to the result list
        courses that have no prereqs, as we DFS
        """
        resSet, res = set(), []
        adj = defaultdict(list)
        visiting = set()

        for cls, req in prerequisites:
            adj[cls].append(req)

        def dfs(i):
            if not adj[i]:
                if i not in resSet:
                    resSet.add(i)
                    res.append(i)
                return True
            if i in visiting:
                return False
            
            visiting.add(i)
            for req in adj[i]:
                if not dfs(req):
                    return False
            visiting.remove(i)
            if i not in resSet:
                resSet.add(i)
                res.append(i)
            adj[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return list(res)
        
