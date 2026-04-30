class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # int -> set
        cols = defaultdict(set) # int -> set
        subboxes = defaultdict(set) # (int, int) -> set 

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue

                # check row
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                # check col
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])
                # check subboxes
                if board[i][j] in subboxes[(i // 3, j // 3)]:
                    return False
                else:
                    subboxes[(i // 3, j // 3)].add(board[i][j])

        return True