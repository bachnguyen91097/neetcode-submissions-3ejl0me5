class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        current_end = 0
        jump = 0

        n = len(nums) 
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jump += 1
                current_end = farthest
        return jump
        