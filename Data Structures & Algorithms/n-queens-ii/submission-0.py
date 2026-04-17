class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag = set()
        antiDiag = set()

        def helper(r):
            if r == n:
                return 1
            total = 0
            for c in range(n):
                if c in cols or (r-c) in diag or (r + c) in antiDiag:
                    continue
                cols.add(c)
                diag.add(r-c)
                antiDiag.add(r+c)

                total += helper(r+1)

                cols.remove(c)
                diag.remove(r-c)
                antiDiag.remove(r+c)
            return total
        return helper(0)
        