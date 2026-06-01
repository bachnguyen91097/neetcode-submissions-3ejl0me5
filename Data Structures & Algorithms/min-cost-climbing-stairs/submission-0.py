class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        goal = len(cost)
        res = float("inf")
        dp = {}
        def helper(i):
            if i >= goal:
                return 0
            if i in dp:
                return dp[i]
            current_cost = cost[i]
            current_cost += min(helper(i+1), helper(i+2))
            dp[i] = current_cost
            return dp[i]
        res = min(helper(0), helper(1))
        return res