class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for flight in flights:
            src_airport, dst_airport, price_dst_airport = flight
            adj[src_airport].append([dst_airport, price_dst_airport])
        heap = [(0, src, 0)]
        visited = {}
        while heap:
            price_airport, airport, stop = heapq.heappop(heap)
            if airport == dst:
                return price_airport
            if stop > k:
                continue
            if airport in visited and visited[airport] <= stop:
                continue
            visited[airport] = stop
            for neighbor in adj[airport]:
                dst_airport, price_dst_airport = neighbor
                heapq.heappush(heap, (price_airport + price_dst_airport, dst_airport, stop + 1))
        return -1