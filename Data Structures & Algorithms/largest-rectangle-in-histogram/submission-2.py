class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # contains highest height currently
        for i, v in enumerate(heights):
            # case 1: v >= top, the rectangle continue
            # case 2: v < top, the rectangle height has to change
            backwards = 0
            while stack and v < stack[-1][0]:
                height, start = stack.pop()
                maxArea = max(maxArea, height * (i - start))
                backwards += 1
            stack.append((v, i - backwards))

        while stack:
            height, start = stack.pop()
            maxArea = max(maxArea, height * (i - start + 1))
        return maxArea



