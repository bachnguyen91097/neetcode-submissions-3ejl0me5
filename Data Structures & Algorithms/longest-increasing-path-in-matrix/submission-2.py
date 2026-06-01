class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        dp = {}
        res = float("-inf")
        def helper(r,c):
            if not(0 <= r < rows and 0 <= c < cols):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            current_path_length = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    current_path_length = max(current_path_length, 1 + helper(nr,nc))
            dp[(r,c)] = current_path_length
            return dp[(r,c)]
        for r in range(rows):
            for c in range(cols):
                res = max(res, helper(r,c))
        return res