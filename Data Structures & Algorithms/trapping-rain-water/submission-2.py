class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        if len(height) == 1:
            return 0

        # find nearest peaks
        while height[l] < height[l + 1]:
            l += 1
        
        while height[r] < height[r - 1]:
            r -= 1
        maxArea = 0
        # step 2: iterate until next peak is met
        while l < r:

            if height[l] < height[r]:
                k = l + 1
                blocks = []
                while height[k] < height[l] and k < r:
                    blocks.append(height[k])
                    k += 1
                minHeight = min(height[l], height[k])
                maxArea += ((k - l - 1) * minHeight) - sum(blocks) 
                l = k
            else:
                q = r - 1
                blocks = []
                while height[q] < height[r] and l < q:
                    blocks.append(height[q])
                    q -= 1
                minHeight = min(height[r], height[q])
                maxArea += ((r - q - 1) * minHeight) - sum(blocks) 
                r = q             
        return maxArea