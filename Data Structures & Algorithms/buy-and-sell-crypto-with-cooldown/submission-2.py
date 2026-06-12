class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def helper(i):
            if i in dp:
                return dp[i]
            if i > len(prices) - 1:
                return 0
            res = 0
            if i < len(prices) - 1:
                j = i + 1
                sell = 0
                while j < len(prices):
                    sell = max(sell, prices[j] - prices[i] + helper(j+2))
                    j += 1
                skip = helper(i+1)
                res = max(sell, skip)
            dp[i] = res
            return res
        return helper(0)
