class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i == len(candidates):
                return

            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            curr.pop()
            dfs(i, total)
            
            return

        dfs(0, 0)
        return res