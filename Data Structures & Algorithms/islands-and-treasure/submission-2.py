class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        def bfs(r, c):
            distance = -1
            seen = set()
            q = [(r, c)]
            while q:
                newq = []
                distance += 1
                for x, y in q:
                    if (
                        0 <= x < ROWS and
                        0 <= y < COLS and
                        (x, y) not in seen and
                        grid[x][y] != "-1" and
                        grid[x][y] >= distance
                    ):
                        grid[x][y] = distance
                        seen.add((x, y))
                        newq.append((x + 1, y))
                        newq.append((x - 1, y))
                        newq.append((x, y + 1))
                        newq.append((x, y - 1))
                q = newq


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: # mark as seen?
                    bfs(r, c)


