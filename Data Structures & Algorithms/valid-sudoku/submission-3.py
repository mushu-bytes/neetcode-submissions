class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        rowSet = { num : set() for num in range(9) }
        colSet = { num : set() for num in range(9) }
        subboxSet = { (num1, num2) : set() for num1 in range(3) for num2 in range(3) }

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rowSet[r] or
                    board[r][c] in colSet[c] or
                    board[r][c] in subboxSet[(r // 3, c // 3)]):
                    
                    return False

                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                subboxSet[(r // 3, c // 3)].add(board[r][c])  

        return True