class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combo = []
        def backtrack(i):
            total = sum(combo)
            if total == target:
                res.append(combo.copy())
            if total >= target or i == len(candidates):
                return

            combo.append(candidates[i])
            backtrack(i + 1)
            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1)
            return

        backtrack(0)
        return res
