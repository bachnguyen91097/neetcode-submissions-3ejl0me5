class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []
        maxProb = {}
        for i in range(len(edges)):
            source, target = edges[i]
            succToTarget = succProb[i]
            adj[source].append([succToTarget, target])
            adj[target].append([succToTarget, source])
        minHeap = []
        heapq.heappush(minHeap, (-1, start_node))
        while minHeap:
            curr_prob, node = heapq.heappop(minHeap)
            curr_prob *= -1

            if node == end_node:
                return curr_prob
            if node in maxProb:
                continue
            maxProb[node] = curr_prob
            for nei_prob, nei in adj[node]:
                new_prob = nei_prob * curr_prob
                if nei not in maxProb:
                    heapq.heappush(minHeap, (-new_prob, nei))
        return 0
