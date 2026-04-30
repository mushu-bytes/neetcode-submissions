class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        def dfs(i: int) -> None:
            comboSum = sum(combo)
            if comboSum >= target:
                if comboSum == target:
                    res.append(combo.copy())
                return
            if i == len(nums):
                return

            combo.append(nums[i])
            dfs(i)
            combo.pop()
            dfs(i + 1)

            return
        dfs(0)
        return res