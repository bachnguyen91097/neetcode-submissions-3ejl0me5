class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        for num in nums:
            currSum = max(0, currSum)
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum