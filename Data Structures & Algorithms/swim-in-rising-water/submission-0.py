class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # min heap to keep track of cell with smallest water elevation
        minHeap = []
        minTime = float("-inf")
        lastRow, lastCol = len(grid), len(grid[0])

        heapq.heappush(minHeap, (grid[0][0], 0, 0))

        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()

        while minHeap:
            current_elevation, r, c = heapq.heappop(minHeap)
            if current_elevation > minTime:
                minTime = current_elevation
            if r == lastRow - 1 and c == lastCol - 1:
                return minTime
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < lastRow and 0 <= nc < lastCol:
                    heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
