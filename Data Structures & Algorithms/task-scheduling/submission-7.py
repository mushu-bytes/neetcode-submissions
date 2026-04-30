class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)
        seen = deque()
        
        time = 0
        while maxHeap or seen:
            if maxHeap:
                nxt = heapq.heappop(maxHeap) + 1
                if nxt != 0:
                    seen.append([nxt, time + n])
            # this line has to happen after the pop,
            # since the free time means basicaly that at the end
            # of the turn its one
            if seen and seen[0][1] == time:
                heapq.heappush(maxHeap, seen.popleft()[0])
            time += 1
        return time

 






