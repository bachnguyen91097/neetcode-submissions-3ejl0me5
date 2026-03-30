class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        
        for time in times:
            u,v,t = time
            adj[u].append([t ,v])
        
        shortest = {}
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        while minHeap:
            t0, n0 = heapq.heappop(minHeap)
            if n0 in shortest:
                continue
            shortest[n0] = t0
            for t, v in adj[n0]:
                if v not in shortest:
                    heapq.heappush(minHeap, (t + t0, v))
        if len(shortest) != n:
            return -1
        else:
            res = 0
            for node in shortest:
                res = max(res,shortest[node])
            return res
