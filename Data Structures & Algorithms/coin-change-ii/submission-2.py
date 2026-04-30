class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        C = [[0] * (amount + 1) for i in range(len(coins))]

        for i in range(len(coins)):
            for a in range(1, amount + 1):
                if a % coins[i] == 0:
                    C[i][a] += 1
                for suba in range(a, 0, -coins[i]):
                    if i - 1 >= 0:
                        C[i][a] += C[i - 1][suba]

        return C[len(coins) - 1][amount]