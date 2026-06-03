class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        numHouses = len(costs)
        numColors = len(costs[0])
        dp = [0] * numColors

        for n in range(numHouses):
            new_dp = [0] * numColors
            for k in range(numColors):
                new_dp[k] = costs[n][k] + min(dp[i] for i in range(numColors) if i != k)
            dp = new_dp
        return min(dp)