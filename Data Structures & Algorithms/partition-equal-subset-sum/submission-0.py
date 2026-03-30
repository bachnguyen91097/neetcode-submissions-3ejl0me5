class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsSum = sum(nums)
        if numsSum % 2 != 0:
            return False
        
        targetSum = numsSum // 2
        n = len(nums)
        
        dp = [[False] * (targetSum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
            for j in range(0, targetSum + 1):
                # we don’t write them as if/else because both choices might be valid, 
                # and we want to keep either one that works.
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]
        
        return dp[n][targetSum]