# solution 2: we go optimal by using DP

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}  # memoization dictionary

        def dfs(i, total):
            # TODO: 1. Base case: what to do when i reaches len(nums)
            if i == len(nums):
                return 1 if total == target else 0

            # TODO: 2. Check memo: return memoized result if exists
            if (i, total) in memo:
                return memo[(i, total)]

            # TODO: 3. Recursive calls: choose +nums[i] or -nums[i]
            add = dfs(i+1, total + nums[i])
            subtract = dfs(i+1, total - nums[i])
            # TODO: 4. Store result in memo
            memo[(i, total)] = add + subtract
            return memo[(i, total)]

        # Start recursion from index 0 and total sum 0
        return dfs(0, 0)
        