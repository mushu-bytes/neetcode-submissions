class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        res = []

        def dfs(i, arr):
            if i == len(nums):
                res.append(perms.copy())
                return

            for j in range(len(arr)):
                perms.append(arr[j])
                dfs(i + 1, arr[:j] + arr[j+1:])
                perms.pop()

            return


        dfs(0, nums)
        return res        


