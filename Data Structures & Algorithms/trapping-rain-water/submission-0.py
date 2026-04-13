class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxHeight = [0]  # will run from beg to end 
        rightMaxHeight = [0] # will run backward from end to beg

        n = len(height)

        currentMaxLeft = height[0]
        for i in range(1, n):
            currentMaxLeft = max(currentMaxLeft, height[i])
            leftMaxHeight.append(currentMaxLeft)
        
        currentMaxRight = height[-1]
        for i in range(n-2, -1, -1):
            currentMaxRight = max(currentMaxRight, height[i])
            rightMaxHeight.append(currentMaxRight)
        rightMaxHeight.reverse()
        res = 0

        for i in range(n):
            trapWater = min(leftMaxHeight[i], rightMaxHeight[i]) - height[i]
            if trapWater > 0:
                res += trapWater
        
        return res



        