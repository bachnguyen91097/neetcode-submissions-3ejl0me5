class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(i, current_comb, current_sum):
            if i >= len(nums) or current_sum > target:
                return
            if current_sum == target:
                result.append(current_comb.copy())
                return
            current_comb.append(nums[i])
            helper(i, current_comb, current_sum + nums[i])
            current_comb.pop()
            helper(i+1, current_comb, current_sum)
        helper(0, [], 0)
        return result