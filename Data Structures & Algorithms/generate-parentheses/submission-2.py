class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(o, c):
            if o == n and c == n:
                res.append("".join(curr))
                return
            
            if o < n:
                curr.append("(")
                backtrack(o + 1, c)
                curr.pop()

            if o > c:
                curr.append(")")
                backtrack(o, c + 1)
                curr.pop()

            return

        backtrack(0, 0)
        return res
     