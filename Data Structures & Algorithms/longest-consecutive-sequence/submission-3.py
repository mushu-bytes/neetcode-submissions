class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        candidates = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in candidates:
                # must be beginning of a sequences
                total = 0
                while num + total in candidates:
                    total += 1
                res = max(total, res)
        return res