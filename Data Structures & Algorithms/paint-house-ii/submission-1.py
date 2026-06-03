class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # O(n * k^2)
        # if not costs:
        #     return 0
        # numHouses = len(costs)
        # numColors = len(costs[0])
        # dp = [0] * numColors

        # for n in range(numHouses):
        #     new_dp = [0] * numColors
        #     for k in range(numColors):
        #         new_dp[k] = costs[n][k] + min(dp[i] for i in range(numColors) if i != k)
        #     dp = new_dp
        # return min(dp)

        #O(n * k)
        if not costs:
            return 0
        numHouses = len(costs)
        numColors = len(costs[0])
        dp = [0] * numColors

        for n in range(numHouses):
            sorted_dp_index = sorted(range(numColors), key=lambda x: dp[x])
            min_dp1, min_dp2 = sorted_dp_index[0], sorted_dp_index[1]
            new_dp = [0] * numColors

            for k in range(numColors):
                if k != min_dp1:
                    new_dp[k] = costs[n][k] + dp[min_dp1]
                else:
                    new_dp[k] = costs[n][k] + dp[min_dp2]
            
            dp = new_dp
        return min(dp)


