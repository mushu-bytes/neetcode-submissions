class Solution:
    def trap(self, height: List[int]) -> int:
        """
        You are given an array of non-negative integers height
        which represent an elevation map.
        Each value height[i] represents the height of a bar,
        which has a width of 1.

        Return the maximum area of water that can be trapped
        between the bars.
        """

        l, r = 0, len(height) - 1
        while l < r and height[l + 1] >= height[l]:
            l += 1
        
        while l < r and height[r - 1] >= height[r]:
            r -= 1
        
        def start_left(l, r):
            area = 0
            while l < r:
                pocket = []
                start = l
                l += 1
                while l < r and height[start] > height[l] :
                    pocket.append(height[l])
                    l += 1
                area += min(height[start], height[l]) * (l - start - 1) - sum(pocket)
                if not l < r:
                    break

                pocket = []
                start = r
                r -= 1
                while l < r and height[start] > height[r]:
                    pocket.append(height[r])
                    r -= 1
                area += min(height[start], height[r]) * (start - r - 1) - sum(pocket)
            return area
        def start_right(l, r):
            area = 0
            while l < r:
                pocket = []
                start = r
                r -= 1
                while l < r and height[start] > height[r]:
                    pocket.append(height[r])
                    r -= 1
                area += min(height[start], height[r]) * (start - r - 1) - sum(pocket)

                if not l < r:
                    break

                pocket = []
                start = l
                l += 1
                while l < r and height[start] > height[l] :
                    pocket.append(height[l])
                    l += 1
                area += min(height[start], height[l]) * (l - start - 1) - sum(pocket)
            return area
        
        print(l, r)
        if height[r] < height[l]:
            return start_right(l, r)
        else:
            return start_left(l, r)




