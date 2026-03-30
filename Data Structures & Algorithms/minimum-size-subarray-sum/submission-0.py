class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')
        curr_size = 0
        curr_sum = 0
        while r < len(nums):
            curr_sum += nums[r]
            if curr_sum < target:
                r += 1
            else:
                while curr_sum >= target:
                    curr_size = r - l + 1
                    res = min(res, curr_size)
                    curr_sum -= nums[l]
                    l += 1
                r += 1
        return res if res != float('inf') else 0
        