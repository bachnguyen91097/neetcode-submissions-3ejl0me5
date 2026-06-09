class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def helper(i1, i2):
            if (i1,i2) in dp:
                return dp[(i1,i2)]
            if i1 < 0 or i2 > len(s) - 1:
                return 0
            res = 0
            if s[i1] == s[i2]:
                res = (1 if i1 == i2 else 2) + helper(i1-1, i2+1)
            else:
                res = max(helper(i1-1, i2), helper(i1, i2+1))
            dp[(i1,i2)] = res
            return res

        answer = float("-inf")
        for i in range(len(s)):
            l1 = helper(i,i)
            l2 = helper(i,i+1)
            answer = max(answer, l1, l2)
        return answer
