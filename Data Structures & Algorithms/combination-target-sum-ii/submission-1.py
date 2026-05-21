class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def helper(i, current_comb, current_sum):
            if current_sum == target:
                result.append(current_comb.copy())
                return
            if i >= len(candidates) or current_sum > target:
                return

            current_comb.append(candidates[i])
            helper(i+1, current_comb, current_sum + candidates[i])
            current_comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, current_comb, current_sum)
        helper(0, [], 0)
        return result