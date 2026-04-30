class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(subset: List[int], arr: List[int]) -> None:
            if not arr:
                res.append(subset)
                return
            for i in range(len(arr)):
                subset.append(arr[i])
                backtrack(subset.copy(), arr[i+1:])
                subset.pop()
            res.append(subset.copy())
            return
        backtrack([], nums)
        return res


