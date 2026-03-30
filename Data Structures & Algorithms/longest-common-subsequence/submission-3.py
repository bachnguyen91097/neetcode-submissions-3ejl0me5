class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        N = n2
        dp = [0] * (N+1)

        for i in range(n1):
            currRow = [0] * (N+1)
            for j in range(n2):
                if text1[i] == text2[j]:
                    currRow[j+1] = 1 + dp[j]
                else:
                    currRow[j+1] = max(currRow[j], dp[j+1])
            dp = currRow
        return dp[N]