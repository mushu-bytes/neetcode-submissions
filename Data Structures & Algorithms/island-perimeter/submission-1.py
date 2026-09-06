class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def get_perimeter(r, c):
            perim = 0
            if r + 1 >= len(grid) or grid[r + 1][c] == 0:
                perim += 1
            if r - 1 < 0 or grid[r - 1][c] == 0:
                perim += 1
            if c + 1 >= len(grid[0]) or grid[r][c + 1] == 0:
                perim += 1
            if c - 1 < 0 or grid[r][c-1] == 0:
                perim += 1
            return perim
            

        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    perimeter += get_perimeter(r, c)
        return perimeter
                    
