class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        def count_func(s):
            num0, num1 = 0, 0
            for c in s:
                if c == "1":
                    num1 += 1
                else:
                    num0 += 1
            return [num0, num1]
        
        def helper(i, num0, num1):
            if i == len(strs):
                return 0
            if (i, num0, num1) in dp:
                return dp[(i, num0, num1)]
            
            curr_num_0, curr_num_1 = count_func(strs[i])
            
            # Option 1: Skip the current string
            res = helper(i + 1, num0, num1)
            
            # Option 2: Include the current string (if constraints allow)
            if num0 + curr_num_0 <= m and num1 + curr_num_1 <= n:
                res = max(res, 1 + helper(i + 1, num0 + curr_num_0, num1 + curr_num_1))
            
            dp[(i, num0, num1)] = res
            return res

        return helper(0, 0, 0)