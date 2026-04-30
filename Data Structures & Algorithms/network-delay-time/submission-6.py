class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # directed graph, no negative edges
        # edges have weights
        adj = defaultdict(list)

        for src, dst, time in times:
            adj[src].append((time, dst))

        # set the distances of each node to infinity, if not target
        distances = {}
        for i in range(1, n + 1):
            if i == k:
                distances[i] = 0
            else:
                distances[i] = float("inf")

        # shortest path tree: return the length of the longest
        # path within the shortest path tree
        q = [(0, k)]
        seen = set()

        while q:
            dist, src = heapq.heappop(q)
            seen.add(src)

            for dist2, dst in adj[src]:
                if distances[dst] > dist + dist2:
                    distances[dst] = dist + dist2
                    heapq.heappush(q, (dist + dist2, dst))

        return max(distances.values()) if len(seen) == n else -1







