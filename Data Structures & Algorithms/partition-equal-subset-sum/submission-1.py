class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum // 2 # capacity
        # nums values are weights

        # dp in T/F states, if T then return T, at the end return F

        dp = [[False] * (target + 1) for _ in range(len(nums))]

        # base case for first item
        for col in range(target + 1):
            dp[0][col] = True if nums[0] == col or col == 0 else False
        
        for r in range(1, len(nums)):
            for c in range(1, target + 1):
                skip = dp[r-1][c]
                include = False
                if nums[r] <= c:
                    include = dp[r-1][c - nums[r]]
                dp[r][c] = skip or include
        return dp[len(nums)-1][target]