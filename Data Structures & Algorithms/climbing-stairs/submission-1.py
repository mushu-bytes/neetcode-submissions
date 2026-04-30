class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        if not n:
            return n

        def backtrack(i):
            if i == n:
                res.append(1)
                return
            if i >= n:
                return


            backtrack(i + 1)
            backtrack(i + 2)
            return

        backtrack(0)
        return len(res)
