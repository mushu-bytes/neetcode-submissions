class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def speed(piles, k):
            count = 0
            for pile in piles:
                count += pile // k
                count = count + 1 if pile % k else count
            return count
        
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            if speed(piles, m) > h:
                l = m + 1
            elif m - 1 and speed(piles, m - 1) <= h:
                r = m - 1
            else:
                return m