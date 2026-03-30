class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numsSum = sum(nums)
        if len(nums) == 1 or numsSum - nums[0] == 0:
            return 0
        if numsSum - nums[-1] == 0:
            return len(nums) - 1
        prefixSum = [0]

        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[i-1] + nums[i-1])
            if prefixSum[i] == numsSum - prefixSum[i] - nums[i]:
                return i
        return -1