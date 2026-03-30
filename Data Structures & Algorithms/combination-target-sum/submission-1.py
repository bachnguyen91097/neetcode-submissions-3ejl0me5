class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        currComb = []
        self.helper(0, currComb, res, nums, target)
        return res

    def helper(self, i, currComb, res, nums, target):
        if target == 0:
            res.append(currComb.copy())
            return
        if i >= len(nums) or target < 0:
            return
        currComb.append(nums[i])
        self.helper(i, currComb, res, nums, target - nums[i])
        currComb.pop()
        self.helper(i + 1, currComb, res, nums, target)
    