class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(idx, current_sum, current_combination):
            if current_sum == target:
                res.append(current_combination.copy())
                return
            if idx > len(nums) - 1 or current_sum > target:
                return
            current_combination.append(nums[idx])
            helper(idx, current_sum + nums[idx], current_combination)
            current_combination.pop()
            helper(idx + 1, current_sum, current_combination)
        helper(0, 0, [])
        return res