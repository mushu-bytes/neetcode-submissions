class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def speed(piles, k):
            count = 0
            for pile in piles:
                count += pile // k
                count = count + 1 if pile % k else count
            return count
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            time = speed(piles, m)
            if time > h:
                l = m + 1
            elif time <= h:
                res = m
                r = m - 1
        return res