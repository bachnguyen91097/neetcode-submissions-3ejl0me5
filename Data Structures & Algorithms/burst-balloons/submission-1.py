class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def helper(l, r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = float("-inf")
            for i in range(l, r+1):
                coins = nums[l - 1] * nums[i] * nums[r+1]
                coins += helper(l, i - 1) + helper(i + 1,r )
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l,r)]
        return helper(1, len(nums) - 2)
        