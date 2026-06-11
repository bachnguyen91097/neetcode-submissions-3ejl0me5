class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []

        for i in range(len(edges)):
            a,b = edges[i]
            sP = succProb[i]
            adj[a].append((b, sP))
            adj[b].append((a, sP))

        maxHeap = [(-1.0, start_node)]
        max_prob = {}

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            if node == end_node:
                return abs(prob)
            if node in max_prob:
                continue
            max_prob[node] = abs(prob)
            for neighbor, prob_to_neighbor in adj[node]:
                if neighbor not in max_prob:
                    heapq.heappush(maxHeap,((prob * prob_to_neighbor), neighbor))
        
        return 0