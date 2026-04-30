class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        map = {}
        for i in range(len(nums)):
            map[i] = nums[i]
            map[i + len(nums)] = nums[i]

        for i in range(len(nums) * 2):
            arr.append(map[i])

        return arr