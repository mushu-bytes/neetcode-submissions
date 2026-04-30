class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        maxCurr = 0
        for n in nums:
            maxCurr = max(maxCurr + n, n)
            maxSum = max(maxCurr, maxSum)
        return maxSum