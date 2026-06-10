class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        n = len(grid)
        min_time = {}
        minHeap = [[grid[0][0],(0,0)]]
        while minHeap:
            e, p = heapq.heappop(minHeap)
            if p in min_time:
                continue
            min_time[p] = e
            for dr, dc in directions:
                nr, nc = p[0] + dr, p[1] + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in min_time:
                    heapq.heappush(minHeap, [max(e,grid[nr][nc]), (nr,nc)])
        return min_time[(n-1,n-1)]