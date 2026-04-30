class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])

        def bfs(coord):
            q = deque([(coord, 0)])
            visited = set(coord)
            while q:
                point, dist = q.popleft()
                x, y = point
                nbrs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                for x1, y1 in nbrs:
                    if (0 <= x1 < rows and
                        0 <= y1 < cols and
                        (x1, y1) not in visited and
                        dist + 1 < grid[x1][y1]):

                        grid[x1][y1] = dist + 1
                        q.append(((x1, y1), dist + 1))
                        visited.add((x1, y1))
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs((r, c))
