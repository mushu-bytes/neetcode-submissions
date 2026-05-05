class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def daysToShip(k, weights):
            i = 0
            res = 0
            while i < len(weights):
                current = 0
                while i < len(weights) and current + weights[i] <= k:
                    current += weights[i]
                    i += 1
                res += 1
            return res

        res = sum(weights)
        l, r = max(weights), res
        while l <= r:
            m = (l + r) // 2
            if daysToShip(m, weights) <= days:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
                