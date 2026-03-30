# Solution 1: brute force solution. Explore
# each path (add path and subtract path)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            # add path
            add = dfs(index + 1, current_sum + nums[index])

            # subtract path
            subtract = dfs(index + 1, current_sum - nums[index])

            return add + subtract
        return dfs(0,0)