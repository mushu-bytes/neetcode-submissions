class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return 0
        s1, s2 = 0, 0
        for i in range(2, len(cost) + 1):
            sol = min(s2 + cost[i - 1], s1 + cost[i - 2])
            s1 = s2
            s2 = sol
        
        return sol