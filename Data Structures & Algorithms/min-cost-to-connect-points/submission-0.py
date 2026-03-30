class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, dist])
                adj[j].append([i, dist])
        visited = set()

        minHeap = [[0, 0]]
        res = 0
        while len(visited) < len(points):
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res += dist
            visited.add(node)
            for neighbor, dist_to_neighbor in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (dist_to_neighbor, neighbor))
        return res