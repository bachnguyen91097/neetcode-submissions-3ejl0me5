class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, row, col):
            if i == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[i] or board[row][col] == "#":
                return False
            
            tmp = board[row][col]
            board[row][col] = "#"

            res = dfs(i+1, row - 1, col) or dfs(i+1, row + 1, col) or dfs(i+1, row, col - 1) or dfs(i+1, row, col + 1)

            board[row][col] = tmp

            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True
        return False