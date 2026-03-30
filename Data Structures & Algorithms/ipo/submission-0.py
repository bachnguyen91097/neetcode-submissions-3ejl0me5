import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # min heap
        minCapital = []

        # max heap
        maxProfit = []

        for c, p in zip(capital, profits):
            heapq.heappush(minCapital, (c,p))

        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)
            if not maxProfit:
                break
            w += -1 * heapq.heappop(maxProfit)
        
        return w