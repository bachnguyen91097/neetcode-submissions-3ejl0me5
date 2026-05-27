class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(idx, current_sum, current_comb):
            if current_sum == target:
                res.append(current_comb.copy())
                return
            if current_sum > target or idx > len(candidates) - 1:
                return
            current_comb.append(candidates[idx])
            helper(idx + 1, current_sum + candidates[idx], current_comb)
            current_comb.pop()
            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            helper(idx + 1, current_sum, current_comb)
        helper(0, 0 , [])
        return res
            