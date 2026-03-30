class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # row
        m = len(obstacleGrid)
        # col
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        prevRow = [0] * n
        for r in range(m-1,-1,-1):
            currRow = [0] * n
            for c in range(n-1,-1,-1):
                if obstacleGrid[r][c] == 1:
                    currRow[c] = 0
                else:
                    if r == m - 1 and c == n - 1:
                        currRow[c] = 1
                    else:
                        right = currRow[c+1] if c + 1 < n else 0
                        down = prevRow[c]
                        currRow[c] = right + down
            prevRow = currRow
        return prevRow[0]
