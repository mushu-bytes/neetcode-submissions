class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search between 1 and max(piles)
        def speed(k_temp):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k_temp)
            return time
        
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if speed(m) <= h:
                r = m 
            else:
                l = m + 1

        return l