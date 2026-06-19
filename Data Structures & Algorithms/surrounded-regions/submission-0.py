from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        O_border = set()
        rows = len(board)
        cols = len(board[0])

        for c in range(cols):
            if board[0][c] == "O":
                O_border.add((0,c))
            if board[rows-1][c] == "O":
                O_border.add((rows-1, c))
        
        for r in range(1,rows-1):
            if board[r][0] == "O":
                O_border.add((r,0))
            if board[r][cols-1] == "O":
                O_border.add((r,cols-1))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        queue = deque(O_border)
        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr, nc) not in O_border:
                    O_border.add((nr, nc))
                    queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in O_border:
                    board[r][c] = "X" 