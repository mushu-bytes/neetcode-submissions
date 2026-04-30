class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)
        maxLength = 0
        for num in nums:
            if num - 1 in hashset:
                continue
            length = 0
            while num + length in hashset:
                length += 1
            maxLength = max(length, maxLength)
        return maxLength
