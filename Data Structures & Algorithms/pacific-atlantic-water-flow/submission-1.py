class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        map_atl = [[False] * cols for _ in range(rows)]
        map_pac = [[False] * cols for _ in range(rows)]

        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        atl_borders = []
        pac_borders = []

        for r in range(rows):
            atl_borders.append([r, cols - 1])
            map_atl[r][cols - 1] = True
            pac_borders.append([r, 0])
            map_pac[r][0] = True
        
        for c in range(cols):
            atl_borders.append([rows - 1, c])
            map_atl[rows-1][c] = True
            pac_borders.append([0, c])
            map_pac[0][c] = True
        
        def bfs(source, ocean):
            queue = deque(source)
            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        queue.append([nr, nc])
                        ocean[nr][nc] = True
        
        bfs(atl_borders, map_atl)
        bfs(pac_borders, map_pac)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if map_atl[r][c] and map_pac[r][c]:
                    res.append([r,c])
        return res


