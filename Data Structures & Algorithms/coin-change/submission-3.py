class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        c = [0] + [-1] * amount
        for i in range(1, amount + 1):
            minCoins = float('inf')
            for coin in coins:
                if i - coin < 0 or c[i - coin] == -1:
                    continue
                minCoins = min(minCoins, c[i - coin])
            if minCoins != float('inf'):
                c[i] = minCoins + 1

        return c[amount]
