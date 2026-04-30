class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        lists = []

        def dfs(i):
            if i == len(nums):
                lists.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
            dfs(i + 1)
            return

        dfs(0)
        return lists
