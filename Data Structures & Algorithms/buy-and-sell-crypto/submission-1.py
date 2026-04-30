class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for r in range(1, len(prices)):
            maxP = max(maxP, prices[r] - prices[l])
            if prices[r] - prices[l] < 0:
                l = r
        return maxP