class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1

        index = 0
        for color in [0, 1, 2]:
            while counter[color]:
                nums[index] = color
                index += 1
                counter[color] -= 1
                
