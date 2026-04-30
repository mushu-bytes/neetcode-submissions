class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        DP Table:
        1. Definition: L[i] is the length of the longest increasing sub
        sequence such that nums[i] is in the sequence
        2. Base Case: L[0] = 1
        3. Solution: L[n]
        4. Formula: L[i] = max(L[j]) + 1, where j < i
        """
        L = [1] * (len(nums))
        for i, v in enumerate(nums):
            for j in range(i):
                if v > nums[j]:
                   L[i] = max(L[j] + 1, L[i])
        return max(L)