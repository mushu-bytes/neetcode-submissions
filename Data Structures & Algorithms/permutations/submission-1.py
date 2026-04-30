class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        def dfs(arr):
            if not arr:
                res.append(perm.copy())
                return

            for i in range(len(arr)):
                perm.append(arr[i])
                dfs( arr[:i] + arr[i+1:] )
                perm.pop()

            return
            
        dfs(nums)
        return res
