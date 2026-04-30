class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # convert list to tuples
        points = list( map(lambda x: tuple(x), points) )

        # create the graph
        adj = defaultdict(list) # point -> (cost, nbr)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = self.mandist(points[i], points[j])
                adj[points[i]].append((dist, points[j]))
                adj[points[j]].append((dist, points[i]))

        seen = set()
        res = 0
        q = [(0, points[0])]
        while q:
            dist, curr = heapq.heappop(q)
            if curr in seen:
                continue
            seen.add(curr)
            res += dist
            for dst, nbr in adj[curr]:
                if nbr not in seen:
                    heapq.heappush(q, (dst, nbr))

        return res

    def mandist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

