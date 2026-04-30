class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (0 <= r < rows and
                0 <= c < cols and
                (r, c) not in seen and
                grid[r][c] == "1"):

                seen.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

            return

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res

