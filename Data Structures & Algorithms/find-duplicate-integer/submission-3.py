class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, 1
        while nums[l] != nums[r]:
            l = (l + 1) % len(nums)
            r = (r + 2) % len(nums)
            if l == r:
                r = (r + 2) % len(nums)
        
        return nums[l]