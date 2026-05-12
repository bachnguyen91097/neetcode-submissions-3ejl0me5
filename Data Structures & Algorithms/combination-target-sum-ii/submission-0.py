class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(idx, current_combination, current_sum):
            if current_sum == target:
                res.append(current_combination.copy())
                return
            if idx >= len(candidates) or current_sum > target:
                return
            
            current_combination.append(candidates[idx])
            helper(idx + 1, current_combination, current_sum + candidates[idx])
            current_combination.pop()
            
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            helper(idx + 1, current_combination, current_sum)
        helper(0, [], 0)
        return res