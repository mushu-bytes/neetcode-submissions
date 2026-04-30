class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search between 1 and max(piles)
        def eat(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total
        
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if eat(m) <= h:
                r = m
            else:
                l = m + 1
        return r
        