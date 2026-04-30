class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            if height[r] < height[l]:
                i = r - 1
                blocks = 0
                while height[i] < height[r]:
                    blocks += height[i]
                    i -= 1
                maxArea += (r - i - 1) * min(height[i], height[r])
                maxArea -= blocks
                r = i

            else:
                i = l + 1
                blocks = 0
                while height[i] < height[l]:
                    blocks += height[i]
                    i += 1
                maxArea += (i - l - 1) * min(height[i], height[l])
                maxArea -= blocks
                l = i

        return maxArea