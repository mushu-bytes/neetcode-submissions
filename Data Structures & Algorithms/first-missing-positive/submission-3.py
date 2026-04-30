class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        FLAG = -1
        one = False
        for i, v in enumerate(nums):
            if v < 1 or v > len(nums):
                nums[i] = 0
            if v == 1:
                one = True

        if not one:
            return 1

        for i in range(len(nums)):
            if nums[i] == 0 or nums[i] == FLAG:
                continue
            index = nums[i] - 1
            if nums[i] != -1:
                nums[i] = 0
            
            while True:
                tmp = nums[index]
                nums[index] = FLAG
                index = tmp - 1
                # this is the bug
                if nums[index] == FLAG or index < 0:
                    break

        for i, v in enumerate(nums):
            if v != -1:
                return i + 1
        return len(nums) + 1




        
