class MedianFinder:

    def __init__(self):
        self.large = [] # minHeap
        self.small = [] # maxHeap
        
    def addNum(self, num: int) -> None:
        # adding the number to whichever heap is correct
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        # correcting size differences
        if len(self.small) > len(self.large) + 1: 
            val = -(heapq.heappop(self.small))
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (self.large[0] + -self.small[0]) / 2.0
        








