class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                nbrs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for x, y in nbrs:
                    if (0 <= x < rows and
                        0 <= y < cols and
                        grid[x][y] != -1 and
                        (x, y) not in visited):
                        q.append((x, y))
                        visited.add((x, y))
            dist += 1


