class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pals = []

        def backtrack(i):
            if i >= len(s):
                res.append(pals.copy())
                return

            for j in range(i, len(s)):
                forward = s[i:j+1]
                backward = forward[::-1]
                if forward == backward:
                    pals.append(s[i:j+1])
                    backtrack(j + 1)
                    pals.pop()

            return

        backtrack(0)
        return res