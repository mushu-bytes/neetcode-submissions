class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        row = ""
        board = [["." for i in range(n)] for nRows in range(n)]
        seen = set()
        def isValid(point):
            x0, y0 = point
            for x, y in seen:
                if (x == x0 or
                    y == y0 or
                    abs(x - x0) == abs(y - y0)):
                    return False
            return True

        def backtrack(i):
            if i == n:
                if len(seen) == n:
                    res.append(["".join(row) for row in board.copy()])
                return
            
            for j in range(n):
                if isValid((i, j)):
                    board[i][j] = "Q"
                    seen.add((i, j))
                    backtrack(i + 1)
                    seen.remove((i, j))
                    board[i][j] = "."
            return

        backtrack(0)
        return res