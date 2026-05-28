class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap,-1*stone)
        while len(maxHeap) > 1:
            firstStone = heapq.heappop(maxHeap) * -1
            secondStone = heapq.heappop(maxHeap) * -1
            if firstStone == secondStone:
                continue
            else:
                heapq.heappush(maxHeap, abs(firstStone - secondStone) * -1)
        return maxHeap[0] * -1 if maxHeap else 0