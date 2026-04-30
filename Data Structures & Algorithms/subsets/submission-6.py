class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
            dfs(i + 1)

            return

        dfs(0)
        return res