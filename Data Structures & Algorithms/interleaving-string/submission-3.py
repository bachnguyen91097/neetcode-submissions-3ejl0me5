class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def helper(i1,i2,i3):
            if i3 == len(s3):
                return True
            if i1 == len(s1) and i2 == len(s2) and i3 != len(s3):
                return False
            if (i1,i2,i3) in dp:
                return dp[(i1,i2,i3)]
            
            res1, res2 = False, False
            if i1 < len(s1) and s1[i1] == s3[i3]:
                res1 = helper(i1+1,i2,i3+1)
            if i2 < len(s2) and s2[i2] == s3[i3]:
                res2 = helper(i1,i2+1,i3+1)
                
            res = res1 or res2
            dp[(i1,i2,i3)] = res
            return res
        return helper(0,0,0)