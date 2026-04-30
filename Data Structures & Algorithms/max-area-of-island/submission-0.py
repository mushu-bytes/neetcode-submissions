class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        res = 0

        def bfs(r, c):
            area = 0
            q = deque([(r, c)])

            while q:
                x, y = q.popleft()
                if (0 <= x < rows and
                    0 <= y < cols and
                    (x, y) not in seen and
                    grid[x][y] == 1):

                    seen.add((x, y))
                    area += 1
                    nbrs = [(x + 1, y), (x - 1, y),
                            (x, y + 1), (x, y - 1)]
                    for n in nbrs:
                        q.append(n)

            return area

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == 1:
                    res = max(bfs(r, c), res)

        return res
