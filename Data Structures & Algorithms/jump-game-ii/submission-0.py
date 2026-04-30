class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        target = len(nums) - 1
        steps = 0
        while i < target:
            if i + nums[i] >= target:
                return steps + 1
            maxJump = 0
            maxJumpIndex = 0
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                if i + j + nums[i + j] > maxJump:
                    maxJumpIndex = i + j
                    maxJump = i + j + nums[i + j]
            i = maxJumpIndex
            steps += 1
        return steps
