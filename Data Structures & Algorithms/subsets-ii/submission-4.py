class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subsets = []
        seen = set()

        def dfs(i):
            if i >= len(nums):
                if tuple(subsets) not in seen:
                    res.append(subsets.copy())
                seen.add(tuple(subsets))
                return

            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
            dfs(i + 1)
            return


        dfs(0)
        return res