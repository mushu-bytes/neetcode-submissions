class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = defaultdict(list)
        for p in points:
            d[self.dist(p)].append(p)
        
        l = list(d.keys())
        heapq.heapify(l)
        res = []
        while k:
            for p in d[heapq.heappop(l)]:
                res.append(p)
                k -= 1
        return res

    def dist(self, p):
        return p[0] ** 2 + p[1] ** 2