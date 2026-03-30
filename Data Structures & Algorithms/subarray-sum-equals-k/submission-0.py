class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0: 1}
        res = 0
        currSum = 0
        for num in nums:
            currSum += num
            diff = currSum - k
            res += hmap.get(diff, 0)
            hmap[currSum] = 1 + hmap.get(currSum, 0)
        return res