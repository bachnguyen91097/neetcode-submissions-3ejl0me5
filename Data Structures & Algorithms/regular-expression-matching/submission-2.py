class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ROWS = len(s)
        COLS = len(p)

        dp = [[False] * (COLS + 1) for _ in range(ROWS + 1)]

        dp[0][0]= True
        for j in range(2, COLS + 1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if p[j-1] != "*":
                    if s[i-1] == p[j-1] or p[j-1] == ".":
                        dp[i][j] = dp[i-1][j-1]
                else:
                    # Zero occurrences of the preceding element
                    dp[i][j] = dp[i][j-2]
                    # One or more occurrences: check if current s char matches preceding p char
                    if s[i-1] == p[j-2] or p[j-2] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[ROWS][COLS]