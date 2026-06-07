class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def helper(i, current_amount):
            if i >= len(coins) or current_amount > amount:
                return 0
            if current_amount == amount:
                return 1
            if (i, current_amount) in dp:
                return dp[(i, current_amount)]
            skip = helper(i + 1, current_amount)
            include = helper(i, current_amount + coins[i])
            dp[(i, current_amount)] = skip + include
            return dp[(i, current_amount)]
        return helper(0,0)
