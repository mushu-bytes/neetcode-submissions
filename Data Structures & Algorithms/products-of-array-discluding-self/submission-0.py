class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            currProd = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                currProd *= nums[j]
            output.append(currProd)
        return output