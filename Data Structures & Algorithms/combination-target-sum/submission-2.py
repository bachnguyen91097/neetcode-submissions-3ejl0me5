class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(idx, current_combination, current_sum):
            if idx >= len(nums) or current_sum > target:
                return
            if current_sum == target:
                res.append(current_combination.copy())
                return
            current_combination.append(nums[idx])
            helper(idx, current_combination, current_sum + nums[idx])
            current_combination.pop()
            helper(idx + 1, current_combination, current_sum)
        helper(0, [], 0)
        return res