class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m % 2 != 0 and m > 0:
                m -= 1
            if nums[m] != nums[m+1] and nums[m] != nums[m-1]:
                return nums[m]
            if nums[m] == nums[m+1]:
                l = m + 2
            else:
                r = m - 1
        return nums[l]