class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for n in nums:
            count[n] += 1
        print(count)
        i = 0
        for k in range(len(count)):
            for j in range(count[k]):
                nums[i] = k
                i += 1       