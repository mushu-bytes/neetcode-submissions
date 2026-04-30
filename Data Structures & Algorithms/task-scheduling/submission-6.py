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
            if seen and seen[0][1] == time:
                heapq.heappush(maxHeap, seen.popleft()[0])
            time += 1
        return time


"""
Map the values to a freq count. From there, ask yourself:
you need a maxheap in order to process the elements in case
of priority: elements that are most frequent must be processed
first, since that would reduce the wait time necessary

Once you have popped from the heap, you need to add it to the queue
This would help us determine when the task could be used next

When adding the item to the queue, you have to attach the 
time which it would be ready, which could be calculated to
time + n (time will function as a global clock)

Each loop would be one timestep. 

Each loop I will check the head of the queue to determine whether
its ready to be enqueued into the heap. Then, I will
pop the next element after / if I enqueue, and readd that new
element into the queue

If the heap is ever empty, then we would just have to increment
timestep and move on. 
"""    







