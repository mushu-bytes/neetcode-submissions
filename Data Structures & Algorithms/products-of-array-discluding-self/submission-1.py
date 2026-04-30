class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        preSum = [1]
        for i in range(len(nums) - 1):
            curr *= nums[i]
            preSum.append(curr)
        
        curr = 1
        postSum = [1]
        for i in range(len(nums) - 1, 0, -1):
            curr *= nums[i]
            postSum.append(curr)
        out = []
        for i in range(len(preSum)):
            out.append(preSum[i] * postSum[-(1 + i)])
        return out
