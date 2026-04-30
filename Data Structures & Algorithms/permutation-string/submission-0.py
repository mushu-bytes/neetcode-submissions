class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        goal = {}
        for c in s1:
            goal[c] = 1 + goal.get(c, 0)
        
        l = 0
        curr = {}
        for r in range(len(s2)):
            curr[s2[r]] = 1 + curr.get(s2[r], 0)
            if (r - l + 1) > len(s1):
                curr[s2[l]] -= 1
                if curr[s2[l]] == 0:
                    del curr[s2[l]]
                l += 1
            print(curr, goal)
            if curr == goal:
                return True
        return curr == goal