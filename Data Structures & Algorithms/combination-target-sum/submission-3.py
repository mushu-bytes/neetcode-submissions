class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []

        def dfs(i):
            if i == len(nums) or sum(curr) >= target:
                if sum(curr) == target:
                    res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i)
            curr.pop()
            dfs(i + 1)
            return

        dfs(0)
        return res     