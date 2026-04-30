class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        My main immediate intuition here is to use a 
        monotonically decreasing stack, mainly because
        of the detail that we are looking only for the
        warmer temperatures.
        
        The idea is that if we have a monotonically decreasing stack,
        then we can check the top of the stack to see if there is anything
        less than the current. Then we can repeatedly check the top.

        I guess we can also store the position as well so we can 
        calc the number of days
        """

        stack = [] # (temp, idx)
        res = [0 for i in range(len(temperatures))]

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, i = stack.pop()
                res[i] = idx - i
                
            stack.append((temp, idx))

        return res







    