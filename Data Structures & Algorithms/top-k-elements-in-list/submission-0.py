class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        min_heap = []
        for num, frequency in nums_counter.items():
            heapq.heappush(min_heap, (-frequency, num))
        
        return [heapq.heappop(min_heap)[1] for _ in range(k)]