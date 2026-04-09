class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        visited = set()
        while q:
            q_length = len(q)
            for i in range(q_length):
                current_row, current_col = q.popleft()
                for direction in directions:
                    row_movement, col_movement = direction
                    new_row = current_row + row_movement
                    new_col = current_col + col_movement
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid[new_row][new_col] != 2147483647 or (new_row, new_col) in visited:
                        continue
                    grid[new_row][new_col] = grid[current_row][current_col] + 1
                    q.append((new_row, new_col))
                    visited.add((new_row,new_col))
        return
        