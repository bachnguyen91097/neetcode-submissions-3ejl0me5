class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # important
                return
            # important 2
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()

            # important 3
            dfs(i+1)
        dfs(0)
        return res