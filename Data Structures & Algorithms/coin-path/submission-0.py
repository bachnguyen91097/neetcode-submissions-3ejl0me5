class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        dp = {}
        answer = []
        n = len(coins)

        def helper(i):
            if coins[i] == -1:
                return [float("inf"), []]
            if i == n - 1:
                return [coins[-1], [i+1]]
            if i in dp:
                return dp[i]
            best_cost = float("inf")
            best_path = []
            for k in range(1, maxJump + 1):
                if i + k >= n:
                    break
                cost, path = helper(i+k)
                total_cost = cost + coins[i]
                if total_cost < best_cost or (total_cost == best_cost and path and [i + 1] + path < best_path):
                    best_cost = total_cost
                    best_path = [i + 1] + path
            dp[i] = [best_cost, best_path]
            return dp[i]
        best_cost, best_path = helper(0)
        return best_path if best_cost != float("inf") else []