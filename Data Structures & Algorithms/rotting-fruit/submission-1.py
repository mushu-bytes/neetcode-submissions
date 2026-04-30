class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        numFresh = 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    numFresh += 1
        
        freshSeen = 0
        seconds = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                nbrs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for x, y in nbrs:
                    if (0 <= x < ROWS and
                        0 <= y < COLS and
                        (x, y) not in visited and
                        grid[x][y] == 1):

                        q.append((x, y))
                        visited.add((x, y))
                        freshSeen += 1
                        grid[x][y] = 2
            seconds += 1
        if numFresh == 0:
            return 0
        return seconds if freshSeen == numFresh else -1






                







