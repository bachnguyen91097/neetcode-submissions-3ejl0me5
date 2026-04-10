from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        # (cost, node, stops)
        heap = [(0, src, 0)]
        
        # dist[node][stops] = min cost
        dist = defaultdict(dict)

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops > k:
                continue

            # ✅ only skip if we have a strictly better cost before
            if stops in dist[node] and dist[node][stops] <= cost:
                continue

            dist[node][stops] = cost

            for nei, price in adj[node]:
                heapq.heappush(heap, (cost + price, nei, stops + 1))

        return -1