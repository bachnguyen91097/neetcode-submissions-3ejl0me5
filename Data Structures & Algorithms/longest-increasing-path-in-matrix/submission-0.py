class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        dp = {}
        res = float("-inf")
        def helper(r,c):
            if not (0 <= r < rows and 0 <= c < cols):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            max_path = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    path_from_neighbor = 1 + helper(nr, nc)
                    max_path = max(path_from_neighbor, max_path)
            dp[(r,c)] = max_path
            return max_path
        for r in range(rows):
            for c in range(cols):
                res = max(res, helper(r,c))
        return res
