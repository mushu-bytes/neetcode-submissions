class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []
        seen = set()

        def dfs(i):
            if i >= len(nums):
                if tuple(sorted(subset)) not in seen:
                    res.append(subset.copy())
                seen.add(tuple(sorted(subset)))
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
            return

        dfs(0)
        return res