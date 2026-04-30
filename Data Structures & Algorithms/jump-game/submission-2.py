class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        i = 0
        while i < target:
            if nums[i] == 0:
                return False
            if nums[i] + i >= target:
                return True

            maxJump = 0
            maxJumpIndex = 0
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    if nums[i + j] + i + j > maxJump:
                        maxJumpIndex = i + j
                    maxJump = max(nums[i + j] + i + j, maxJump)
                
            i = maxJumpIndex
            
        return True
