class Solution:
    def rob(self, nums: List[int]) -> int:
        m1 = nums[0]
        if len(nums) == 1:
            return m1
        m2 = max(m1, nums[1])

        for i in range(2,len(nums)):
            temp = max(m1 + nums[i], m2)
            m1 = m2
            m2 = temp

        return m2