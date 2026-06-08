class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def helper(i1, i2):
            # insert into word1
            if i1 == len(word1):
                return len(word2) - i2
            # delete from word1
            if i2 == len(word2):
                return len(word1) - i1
            if (i1,i2) in dp:
                return dp[(i1,i2)]
            if word1[i1] == word2[i2]:
                res = helper(i1+1,i2+1)
            else:
                insert_option = 1 + helper(i1,i2+1)
                delete_option = 1 + helper(i1 + 1, i2)
                replace_option = 1 + helper(i1+1,i2+1)
                res = min(insert_option, delete_option, replace_option)
            dp[(i1,i2)] = res
            return res
        return helper(0, 0)