class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(p, visited, prevHeight):
            r, c = p
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                p not in visited and
                heights[r][c] >= prevHeight
            ):
                visited.add(p)
                dfs((r + 1, c), visited, heights[r][c])
                dfs((r - 1, c), visited, heights[r][c])
                dfs((r, c + 1), visited, heights[r][c])
                dfs((r, c - 1), visited, heights[r][c])
            return
        
        # PACIFIC
        PAC = set()
        for r in range(ROWS):
            dfs((r, 0), PAC, heights[r][0])

        for c in range(COLS):
            dfs((0, c), PAC, heights[0][c])

        # Atlantic
        ATL = set()
        for r in range(ROWS):
            dfs((r, COLS - 1), ATL, heights[r][COLS - 1])

        for c in range(COLS):
            dfs((ROWS - 1, c), ATL, heights[ROWS - 1][c])

        return list(PAC.intersection(ATL))
