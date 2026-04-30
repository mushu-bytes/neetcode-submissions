class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, index)
        res = [0 for t in temperatures]
        for i, v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((v, i))
        return res


