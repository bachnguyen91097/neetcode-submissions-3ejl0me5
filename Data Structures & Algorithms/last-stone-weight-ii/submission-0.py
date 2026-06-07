class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        dp = {}

        def helper(i, current_sum):
            if i > len(stones) - 1:
                return current_sum
            if (i, current_sum) in dp:
                return dp[(i, current_sum)]
            res = helper(i+1, current_sum)
            if current_sum + stones[i] <= target:
                res = max(res, helper(i+1, current_sum + stones[i]))
            dp[(i, current_sum)] = res
            return dp[(i, current_sum)]
        close = helper(0, 0)
        return sum(stones) - 2 * close