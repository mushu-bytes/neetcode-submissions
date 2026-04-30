class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = 0
        
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1

        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False