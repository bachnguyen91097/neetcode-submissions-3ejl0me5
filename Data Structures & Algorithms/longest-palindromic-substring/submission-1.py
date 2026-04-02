class Solution:
    def longestPalindrome(self, s: str) -> str:
        def buildPalindromeDP(s):
            n = len(s)
            dp = [[False] * n for _ in range(n)]
            for i in range(n-1,-1,-1):
                for j in range(i,n):
                    if i == j:
                        dp[i][j] = True
                    elif j - i <= 1 and s[i] == s[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
            return dp
        maxLength = 0
        maxDP = (0,0)
        dp = buildPalindromeDP(s)
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dp[i][j]:
                    if j - i + 1 > maxLength:
                        maxLength = j - i + 1
                        maxDP = (i,j)
        i,j = maxDP
        return s[i:j+1]
        