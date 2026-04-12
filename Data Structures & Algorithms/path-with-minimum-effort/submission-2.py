class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        rows = len(heights)
        cols = len(heights[0])
        visited = set()
        minHeap = [(0, 0, 0)]
        while minHeap:
            current_diff, current_r, current_c = heapq.heappop(minHeap)
            if (current_r, current_c) in visited:
                continue
            visited.add((current_r, current_c))
            if (current_r, current_c) == (rows - 1, cols - 1):
                return current_diff
            current_height = heights[current_r][current_c]
            for d in directions:
                new_r = current_r + d[0]
                new_c = current_c + d[1]
                if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
                    continue
                new_height = heights[new_r][new_c]
                new_diff = max(current_diff,abs(new_height - current_height))
                heapq.heappush(minHeap, (new_diff, new_r, new_c))
        return 0