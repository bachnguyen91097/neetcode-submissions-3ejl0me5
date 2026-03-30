class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = cnt = 0
        sign = -1
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                cnt = cnt + 1 if sign == 0 else 1
                sign = 1
            elif arr[i-1] > arr[i]:
                cnt = cnt + 1 if sign == 1 else 1
                sign = 0
            else:
                cnt = 0
                sign = -1
            res = max(res, cnt)
        return res + 1