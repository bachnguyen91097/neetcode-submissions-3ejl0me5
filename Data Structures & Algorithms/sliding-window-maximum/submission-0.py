class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        
        res = [-max_heap[0][0]]

        for r in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            while max_heap[0][1] <= r - k:
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])
        
        return res