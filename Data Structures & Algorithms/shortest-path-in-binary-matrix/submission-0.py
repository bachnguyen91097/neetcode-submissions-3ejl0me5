from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        queue = deque()
        visited = set()
        queue.append([0,0,1])
        visited.add((0,0))
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,-1],[1,1],[-1,-1],[-1,1]]
        while queue:
            current = queue.popleft()
            for direction in directions:
                nr = current[0] + direction[0]
                nc = current[1] + direction[1]
                if nr == n - 1 and nc == n-1:
                    return current[2] + 1
                if nr < 0 or nc < 0 or nr >= n or nc >= n or (nr,nc) in visited or grid[nr][nc] == 1:
                    continue
                visited.add((nr,nc))
                new_dist = current[2] + 1
                queue.append([nr,nc,new_dist])
        return -1
