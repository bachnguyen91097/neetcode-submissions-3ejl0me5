class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        count = 0
        curr_sum = 0
        for i in range(k):
            curr_sum += arr[i]
        while r < len(arr):
            if curr_sum / k >= threshold:
                count += 1
            l += 1
            r += 1
            curr_sum -= arr[l-1]
            if r < len(arr):
                curr_sum += arr[r]
        return count