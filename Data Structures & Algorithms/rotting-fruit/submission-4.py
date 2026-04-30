class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        seen = set()
        q = []
        clock = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q:
            newq = []
            for x, y in q:
                if (
                    0 <= x < ROWS and
                    0 <= y < COLS and
                    (grid[x][y] == 2 or grid[x][y] == 1) and
                    (x, y) not in seen
                ):
                    seen.add((x, y))
                    newq.append((x, y + 1))
                    newq.append((x, y - 1))
                    newq.append((x + 1, y))
                    newq.append((x - 1, y))
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                    if fresh == 0:
                        return clock
            q = newq.copy()
            clock += 1
        if fresh == 0:
            return clock
        return -1







                







