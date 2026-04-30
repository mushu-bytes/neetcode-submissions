class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            maxA = max(maxA, area)
            if heights[r] > heights[l]:
                l = l + 1
            else:
                r = r - 1
        return maxA 
