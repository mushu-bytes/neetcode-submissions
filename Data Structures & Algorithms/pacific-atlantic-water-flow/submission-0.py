class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights) - 1, len(heights[0]) - 1
        res = []

        def bfs(point):
            q = deque([point])
            visited = set()
            visited.add(point)
            PAC, ATL = False, False
            while q:
                r, c = q.popleft()
                nbrs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                if r == 0 or c == 0:
                    PAC = True
                if r == ROWS or c == COLS:
                    ATL = True
                if PAC and ATL:
                    return True
                
                for x, y in nbrs:
                    if (0 <= x <= ROWS and
                        0 <= y <= COLS and
                        (x, y) not in visited and
                        heights[x][y] <= heights[r][c]):
                        
                        q.append((x, y))
                        visited.add((x, y))

            return False

        for r in range(ROWS + 1):
            for c in range(COLS + 1):
                if bfs((r, c)):
                    res.append((r, c))
        return res