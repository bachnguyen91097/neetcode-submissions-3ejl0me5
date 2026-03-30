import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        # Create a max heap
        heapq.heapify(stones)

        while len(stones) > 1:
            heavy1 = -heapq.heappop(stones)
            heavy2 = -heapq.heappop(stones)
            if heavy1 == heavy2:
                continue
            elif heavy1 < heavy2:
                heapq.heappush(stones, -(heavy2 - heavy1))
            else:
                heapq.heappush(stones, -(heavy1 - heavy2))
        
        return -stones[0] if stones else 0