class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(numOpen, numClose):
            if numOpen == numClose == n:
                res.append("".join(stack))
                return
            
            if numOpen < n:
                stack.append("(")
                backtrack(numOpen + 1, numClose)
                stack.pop()

            if numOpen > numClose:
                stack.append(")")
                backtrack(numOpen, numClose + 1)
                stack.pop()

        backtrack(0, 0)
        return res
            

            
