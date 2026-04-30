class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in nums:
            length = 0
            if num - 1 not in seen:
                curr = num
                while curr in seen:
                    curr += 1
                    length += 1
            longest = max(longest, length)
            
        return longest