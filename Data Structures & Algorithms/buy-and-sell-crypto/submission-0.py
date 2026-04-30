class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        for r in range(len(prices)):
            maxP = max(prices[r] - prices[l], maxP)
            if prices[r] < prices[l]:
                l = r
        return maxP
