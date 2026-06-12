class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i,len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj[(x1,y1)].append((cost, (x2,y2)))
                adj[(x2,y2)].append((cost, (x1,y1)))
        
        x0, y0 = points[0]
        minHeap = [(0, (x0,y0))]

        ans = 0
        visited = set()
        while len(visited) != len(points):
            cost, (x,y) = heapq.heappop(minHeap)
            if (x,y) in visited:
                continue
            ans += cost
            visited.add((x,y))
            for cost, neighbor in adj[(x,y)]:
                if neighbor in visited:
                    continue
                heapq.heappush(minHeap, (cost, neighbor))
        return ans