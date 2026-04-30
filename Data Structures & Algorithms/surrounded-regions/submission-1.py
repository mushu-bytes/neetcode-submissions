class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def bfs(p, visited):
            q = deque([p])
            visited.add(p)
            surroundable = True
            while q:
                r, c = q.popleft()
                nbrs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for x, y in nbrs:
                    if (
                        0 <= x < ROWS and
                        0 <= y < COLS and
                        (x, y) not in visited and
                        board[x][y] == "O"
                    ):
                        visited.add((x, y))
                        q.append((x, y))
                if (r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1):
                    surroundable = False
            return surroundable

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    visited = set()
                    if bfs((r, c), visited):
                        for x, y in visited:
                            board[x][y] = "X"


        

        