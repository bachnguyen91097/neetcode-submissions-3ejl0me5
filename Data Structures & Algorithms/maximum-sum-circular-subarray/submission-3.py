class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        for num in nums:
            currSum = max(0, currSum)
            currSum += num
            maxSum = max(maxSum, currSum)

        totalSum = sum(nums)
        currSum2 = 0
        minSum = nums[0]
        for num in nums:
            currSum2 = min(0, currSum2)
            currSum2 += num
            minSum = min(minSum, currSum2)
        
        if maxSum < 0:
            return maxSum
        return max(maxSum, totalSum - minSum)