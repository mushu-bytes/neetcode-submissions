class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        """
        1. l < m < r [1, 2, 3, 4, 5, 6] --> move right down
        2. l < m > r [3, 4, 5, 6, 1, 2] --> move left up
        3. l > m < r [6, 1, 2, 3, 4, 5] --> move right down recurse
        
        [3, 4, 5, 6, 1, 2]
        first iteration:
        l = 0, m = 2, r = 5 (3, 5, 2)
        second it:
        l = 3, m = 4, r = 5 (6, 1, 2)
        third it:
        l = 3, m = 3, r = 4 (6, 6, 1)
        """
        minimum = nums[r]
        while l < r:
            m = (l + r) // 2
            if nums[l] < nums[m] and nums[m] < nums[r]:
                r = m
            elif nums[l] <= nums[m] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            minimum = min(minimum, nums[r])

        return minimum