class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        res = []
        curr = 1
        for num in nums:
            prefix.append(curr)
            curr *= num

        curr = 1
        for num in nums[::-1]:
            postfix.append(curr)
            curr *= num

        for i in range(len(nums)):
            res.append(prefix[i] * postfix[-(i + 1)])
        return res