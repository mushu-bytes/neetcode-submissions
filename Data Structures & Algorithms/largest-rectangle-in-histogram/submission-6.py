class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Given an array of integer heights, return the area
        of the largest rectangle that can be formed among
        the bars:
        i.e maximize the height / width of the rectangle

        Observations:
        - Not a two pointer problem because we need to know the
        minimum height anywhere along the rectangle
        - I need to consider horizontal and vertical rectangles
        - at any given point, I have to consider all possible
        rectangles
        - A rectangle between a range of incides is only as tall
        as the minimal value. 
        - Can I keep a stack, where the bottom height is up first?
        the idea is that if I encounter a shorter height, than that ends some of the 
        rectangles that I must consider. I also need to track the index of its
        start.
        - I think the stack must be monotonically increasing. If we see
        a smaller height, than we pop all of the previous heights since its
        the end of the line for them.
        """

        maxArea = 0
        stack = [] # (1, 1) (2, 3) (2, 4) (4, 5)

        for i in range(len(heights)):
            newStart = i
            while stack and heights[i] < stack[-1][0]:
                # consider all rectangles ending HERE (so we consider the previous index i - 1 for width)
                prevHeight, prevIndex = stack.pop()
                prevArea = prevHeight * (i - prevIndex)
                maxArea = max(maxArea, prevArea)
                if prevHeight >= heights[i]:
                    newStart = prevIndex
            
            stack.append((heights[i], newStart))

        # found edge case: once we see a lower height, we have to backtrack to see where that height would be valid from
        while stack:
            prevHeight, prevIndex = stack.pop()
            prevArea = prevHeight * (len(heights) - prevIndex)
            maxArea = max(maxArea, prevArea)

        return maxArea


