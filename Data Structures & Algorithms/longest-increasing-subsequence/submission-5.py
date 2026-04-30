class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [0 for _ in range(len(nums))]
        DP[0] = 1

        for i in range(1, len(nums)):
            maxPrev = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxPrev = max(maxPrev, DP[j])
            DP[i] = 1 + maxPrev

        return max(DP)
