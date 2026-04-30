class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = {}
        for c in hand:
            counter[c] = 1 + counter.get(c, 0)

        keys = list(counter.keys())
        heapq.heapify(keys)

        while keys:
            curr = keys[0]
            for i in range(curr, curr + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != keys[0]:
                        return False
                    heapq.heappop(keys)
        return True
                

        

