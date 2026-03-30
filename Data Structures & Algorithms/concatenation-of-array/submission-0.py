class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(len(nums)):
            ans.append(nums[i])
        for j in range(len(nums)):
            ans.append(nums[j])
        return ans