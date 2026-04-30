class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1
        while l <= r:
            mid = l + (r - l) // 2
            mid_row = mid // n
            mid_col = mid % n
            print(mid, mid_row, mid_col)
            if matrix[mid_row][mid_col] < target:
                l = mid + 1
            elif matrix[mid_row][mid_col] > target:
                r = mid - 1
            else:
                return True

        return False