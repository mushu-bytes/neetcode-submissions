class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)
        while stones:
            print(stones)
            s1 = -heapq.heappop(stones)
            if not stones:
                return s1
            s2 = -heapq.heappop(stones)
            if abs(s1 - s2) != 0:
                heapq.heappush(stones, -abs(s1 - s2))
        return 0