class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        You are given an integer n. 
        Return all well-formed parentheses strings that you 
        can generate with n pairs of parentheses.
        """

        strings = []

        def backtrack(o: int, c: int, current: List[str]):
            if o == 0 and c == 0:
                strings.append("".join(current.copy()))
                return

            if o < c:
                current.append(")")
                backtrack(o, c - 1, current)
                current.pop()
            
            if o > 0:
                current.append("(")
                backtrack(o - 1, c, current)
                current.pop()
            return

        backtrack(n, n, [])
        return strings
