class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if m == 0 and nums[m] > nums[m+1]:
                return 0
            if m == n - 1 and nums[m] > nums[m-1]:
                return n - 1
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m] > nums[m-1] and nums[m] <= nums[m+1]:
                l = m + 1
            elif nums[m] <= nums[m-1] and nums[m] > nums[m+1]:
                r = m
            else:  # valley case: nums[m] <= nums[m-1] and nums[m] <= nums[m+1]
                l = m + 1  # either direction works, peak exists on right
        return l

        