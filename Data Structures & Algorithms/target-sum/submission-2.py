class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)

        def helper(i, current_sum):
            if i == n:
                return 1 if current_sum == target else 0
            if (i, current_sum) in dp:
                return dp[(i, current_sum)]
            
            current_way = helper(i+1, current_sum + nums[i]) + helper(i+1, current_sum - nums[i])
            dp[(i, current_sum)] = current_way
            return dp[(i, current_sum)]
        return helper(0, 0)