class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i, r, c):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or board[r][c] == "#":
                return False
            temp = board[r][c]
            board[r][c] = "#"
            for moveR, moveC in directions:
                if dfs(i + 1, r + moveR, c + moveC):
                    return True
            board[r][c] = temp
            return False
        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True
        return False
        