class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        res = 0
        def dfs(r,c, visit):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            return (1 + dfs(r+1,c,visit) +
            dfs(r-1,c,visit) +
            dfs(r,c+1,visit) +
            dfs(r,c-1,visit))
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res,dfs(r,c,visit))
        return res