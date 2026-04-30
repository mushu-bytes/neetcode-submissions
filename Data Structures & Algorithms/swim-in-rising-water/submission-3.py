class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # priority queue bfs while tracking the max elevation seen up to 
        # shortest path from (0, 0) to (SIZE - 1, SIZE - 1)
        SIZE = len(grid)
        # edge weights correspond to min(elevation distance, 0)
        pq = [(grid[0][0], (0, 0))] # weight, point
        parents = {} # point -> point
        dist = {} # point -> dist

        while pq:
            weight, point = heapq.heappop(pq)
            x, y = point
            nbrs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

            for x0, y0 in nbrs:
                if (0 <= x0 < SIZE and
                    0 <= y0 < SIZE and
                    (x0, y0) != (0, 0) and
                    dist.get((x0, y0), float('inf')) > max(grid[x0][y0], weight)):

                    dist[(x0, y0)] = max(grid[x0][y0], weight)
                    parents[(x0, y0)] = point
                    heapq.heappush(pq, (dist[(x0, y0)], (x0, y0)))

        # loop through parent dictionary and check for 0, 0
        i = (SIZE - 1, SIZE - 1)
        res = 0
        while i != (0, 0):
            res = max(res, grid[i[0]][i[1]])
            i = parents[i]
        res = max(res, grid[i[0]][i[1]])
        return res



