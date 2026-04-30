class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        maxP = 0
        for i in range(1, len(prices)):
            if prices[i] > prev:
                maxP += prices[i] - prev
            prev = prices[i]

        return maxP