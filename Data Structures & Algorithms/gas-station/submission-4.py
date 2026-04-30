class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        if sum(cost) > sum(gas):
            return -1
        gasLevel = 0

        for j in range(len(gas)):
            gasLevel += gas[j] - cost[j]
            if gasLevel < 0:
                i = j + 1
                gasLevel = 0

        return i
