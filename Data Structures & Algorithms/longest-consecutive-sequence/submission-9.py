class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        heapq.heapify(nums)
        max_ans = float("-inf")
        res = 1
        curr = heapq.heappop(nums)
        while nums:
            next_num = heapq.heappop(nums)
            if curr + 1 == next_num:
                res += 1
                max_ans = max(max_ans, res)
            elif curr == next_num:
                continue
            else:
                res = 1
            curr = next_num
        return max_ans if max_ans != float("-inf") else 1
