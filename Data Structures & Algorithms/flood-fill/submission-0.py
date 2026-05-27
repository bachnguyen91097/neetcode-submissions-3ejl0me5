from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start == color:
            return image
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        rows = len(image)
        cols = len(image[0])
        queue = deque()
        queue.append([sr,sc])
        while queue:
            cr, cc = queue.popleft()
            image[cr][cc] = color
            for dr,dc in directions:
                nr,nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start:
                    queue.append([nr,nc])
        return image        


        