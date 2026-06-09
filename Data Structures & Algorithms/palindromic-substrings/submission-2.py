class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        def helper(i1, i2):
            if i1 < 0 or i2 > len(s) - 1:
                return 0
            res = 0
            if s[i1] == s[i2]:
                res = 1 + helper(i1-1 ,i2+1)
            dp[(i1,i2)] = res
            return res
        ans = 0
        for i in range(len(s)):
            ans += helper(i,i) + helper(i, i+1)
        return ans
