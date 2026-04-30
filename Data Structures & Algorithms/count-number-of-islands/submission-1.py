class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()

        def dfs(i, j):
            if (
                0 <= i < len(grid) and
                0 <= j < len(grid[0]) and
                grid[i][j] == "1" and
                (i,j) not in seen
            ):

                seen.add((i, j))
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j - 1)

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in seen and grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res

