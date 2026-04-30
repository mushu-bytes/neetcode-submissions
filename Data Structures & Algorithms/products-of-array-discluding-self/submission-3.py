class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pfx = []
        curr = 1
        for num in nums:
            pfx.append(curr)
            curr *= num

        curr = 1
        sfx = []
        for i in range(len(nums) - 1, -1, -1):
            sfx.append(curr)
            curr *= nums[i]

        sfx = sfx[::-1]
        output = []
        for i in range(len(pfx)):
            output.append(pfx[i] * sfx[i])
        return output
