class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            # if m is 0 or prev is greater
            if nums[m - 1] > nums[m]:
                return nums[m]
            else:
                if nums[m] > nums[r]:
                    l = m + 1
                elif nums[m] < nums[r]:
                    r = m - 1
                else:
                    return nums[m]
        