class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
       # Set to keep track if queen in same column, diagnol or anti-diagnol
       cols = set()
       diagnols = set()
       antiDiagnols = set() 

       # final result to return
       result = []

       # board to hold current result
       board = []

       def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or row - col in diagnols or row + col in antiDiagnols:
                continue
            cols.add(col)
            diagnols.add(row - col)
            antiDiagnols.add(row + col)
            board.append(['.'] * n)
            board[-1][col] = 'Q'
            backtrack(row + 1)
            cols.remove(col)
            diagnols.remove(row - col)
            antiDiagnols.remove(row + col)
            board.pop()

       backtrack(0)
       return result