from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        level = 0
        while fresh > 0 and queue:
            current_queue_len = len(queue)
            for i in range(current_queue_len):
                current = queue.popleft()
                r = current[0]
                c = current[1]
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue
                    queue.append([nr,nc])
                    fresh -= 1
                    grid[nr][nc] = 2
            level += 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return level if fresh == 0 else -1