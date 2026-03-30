class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currSet, subSets = [], []
        def helper(i, nums, currSet, subSets):
            if i >= len(nums):
                subSets.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            helper(i+1, nums, currSet, subSets)
            currSet.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i+1, nums, currSet, subSets)
        helper(0, nums, currSet, subSets)
        return subSets