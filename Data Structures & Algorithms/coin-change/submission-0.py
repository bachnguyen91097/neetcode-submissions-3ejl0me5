class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        n = len(coins)
        res = -1

        def helper(i, current_amount):
            if current_amount == amount:
                return 0
            if i > n - 1 or current_amount > amount:
                return float("inf")
            if (i, current_amount) in dp:
                return dp[(i, current_amount)]
            # skip case
            number_of_coins = helper(i+1, current_amount)
            # include case
            if coins[i] + current_amount <= amount:
                number_of_coins = min(number_of_coins, 1 + helper(i, current_amount + coins[i]))
            dp[(i, current_amount)] = number_of_coins
            return dp[(i, current_amount)]
        res = helper(0, 0)
        return res if res != float("inf") else -1