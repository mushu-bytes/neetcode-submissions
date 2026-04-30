class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:         
        nums = [0] + nums
        ROWS, COLS = len(nums), sum(nums) * 2 + 1
        TS = [[0 for i in range(COLS)] for i in range(ROWS)]
        
        if target + sum(nums) >= COLS:
            return 0

        for r in range(ROWS):
            for c in range(-sum(nums), sum(nums) + 1):
                realC = c + sum(nums)
                if r - 1 >= 0:
                    if realC + nums[r] < COLS:
                        TS[r][realC] += TS[r - 1][realC + nums[r]]
                    if realC - nums[r] >= 0:
                        TS[r][realC] += TS[r - 1][realC - nums[r]]
                else:
                    if nums[r] == c or -nums[r] == c:
                        TS[r][realC] += 1

        return TS[ROWS - 1][target + sum(nums)]
                
