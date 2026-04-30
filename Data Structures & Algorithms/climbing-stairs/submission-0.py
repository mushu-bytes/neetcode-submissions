class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0

        table = [1, 1]
        for i in range(2, n + 1):
            table.append(table[i - 1] + table[i - 2])

        return table[n]
