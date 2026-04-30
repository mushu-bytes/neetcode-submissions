class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        sums = set()
        sums.add(0)
        if sum(nums) % 2:
            return False

        for i in range(len(nums)):
            nextSums = set()
            for t in sums:
                if (t + nums[i]) == target:
                    return True

                nextSums.add(nums[i] + t)
                nextSums.add(t)

            sums = nextSums
            
        return False






