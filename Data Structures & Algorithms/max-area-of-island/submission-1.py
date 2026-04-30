class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        seen = set()

        def bfs(r, c):
            size = 0
            q = deque([(r, c)])
            while q:
                curr_r, curr_c = q.popleft()
                if (
                    (curr_r, curr_c) not in seen and
                    0 <= curr_r < ROWS and
                    0 <= curr_c < COLS and
                    grid[curr_r][curr_c] == 1
                ):

                    seen.add((curr_r, curr_c))
                    size += 1
                    q.append((curr_r + 1, curr_c))
                    q.append((curr_r - 1, curr_c))
                    q.append((curr_r, curr_c + 1))
                    q.append((curr_r, curr_c - 1))

            return size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(bfs(r, c), res)

        return res

        