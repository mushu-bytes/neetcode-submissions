class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ROWS, COLS = len(prices), len(prices)
        maxP = [[0 for i in range(COLS)] for i in range(ROWS)]
        maxSell = [0] * COLS
        maxCurr = 0

        for i in range(ROWS):
            for j in range(COLS):
                if j > i:
                    maxP[i][j] = prices[j] - prices[i]
                    if i - 2 >= 0:
                        maxPast = 0
                        for k in range(i-1):
                            maxPast = max(maxSell[k], maxPast)
                        maxP[i][j] += maxPast
                        
                    maxSell[j] = max(maxSell[j], maxP[i][j])
                    maxCurr = max(maxCurr, maxP[i][j])

        return maxCurr
        


        