# Optimal solution: Expand around center

class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l,r,s):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt
        res = 0
        for i in range(len(s)):
            res += expand(i,i,s)
            res += expand(i,i+1,s)
        return res