class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        l1 = len(text1)
        l2 = len(text2)

        def helper(i1, i2):
            if i1 >= l1 or i2 >= l2:
                return 0
            if (i1, i2) in dp:
                return dp[(i1,i2)]
            res = 0
            if text1[i1] == text2[i2]:
                res = 1 + helper(i1+1, i2+1)
            res = max(res, helper(i1+1, i2), helper(i1, i2+1))
            dp[(i1,i2)] = res
            return dp[(i1,i2)]
        return helper(0,0)