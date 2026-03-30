class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        idx_top_row = 0
        idx_last_row = m - 1 
        while idx_top_row <= idx_last_row:
            mid_row = idx_top_row + (idx_last_row - idx_top_row) // 2
            if matrix[mid_row][0] > target:
                idx_last_row = mid_row - 1
            elif matrix[mid_row][-1] < target:
                idx_top_row = mid_row + 1
            else:
                break
        if not (idx_top_row <= idx_last_row):
            return False
        
        target_row = idx_top_row + (idx_last_row - idx_top_row) // 2
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[target_row][m] > target:
                r = m - 1
            elif matrix[target_row][m] < target:
                l = m + 1
            else:
                return True
        return False
        