class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the longest consecutive sequence is the longest distinct
        # sequence of integers that appears in the list
        # essentially, you have to be able to construct a consecutive
        # sequence of integers that is long as possible.
        # I think we have to exploit this consecutive feature.
        # we also don't know if its ordered.
        # I think the key is that you can track what numbers come in the list,
        # then you can check if its the start of a sequence by checking the hashset
        seen = set(nums)
        longest = 0

        for num in nums:
            curr = num
            # check if its a start of a sequence
            if curr - 1 not in seen:
                count = 0
                while curr in seen:
                    count += 1
                    curr += 1
                longest = max(longest, count)

        return longest