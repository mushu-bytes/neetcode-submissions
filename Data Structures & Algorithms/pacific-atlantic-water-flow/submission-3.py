class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS from both Pacific and Atlantic sides.
        ROWS, COLS = len(heights), len(heights[0])
        PAC = set()
        ATL = set()
        def dfs(r, c, visited):
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                visited.add((x, y))
                directions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                for x_n, y_n in directions:
                    if (
                        0 <= x_n < ROWS and
                        0 <= y_n < COLS and
                        (x_n, y_n) not in visited and 
                        heights[x_n][y_n] >= heights[x][y]
                    ):
                        stack.append((x_n, y_n))
            return
    
        for r in range(ROWS):
            dfs(r, 0, PAC)
            dfs(r, COLS - 1, ATL)

        for c in range(COLS):
            dfs(0, c, PAC)
            dfs(ROWS - 1, c, ATL)


        return list(PAC.intersection(ATL))

        