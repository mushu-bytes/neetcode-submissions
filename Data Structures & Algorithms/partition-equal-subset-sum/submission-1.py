class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        diffs = set()
        diffs.add(nums[0])
        for i in range(1, len(nums)):
            newDiffs = set()
            for d in diffs:
                newDiffs.add(abs(nums[i] + d))
                newDiffs.add(abs(nums[i] - d))
            diffs.clear()
            diffs = newDiffs
        return 0 in diffs


