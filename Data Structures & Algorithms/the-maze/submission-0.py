class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start == destination:
            return True
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows = len(maze)
        cols = len(maze[0])
        q = deque()
        visited = {(start[0], start[1])}        
        q.append(start)
        while q:
            q_length = len(q)
            for i in range(q_length):
                currRow, currCol = q.popleft()
                for moveRow, moveCol in directions:
                    newRow = currRow + moveRow
                    newCol = currCol + moveCol
                    while 0 <= newRow < rows and 0 <= newCol < cols and maze[newRow][newCol] != 1:
                        newRow += moveRow
                        newCol += moveCol
                    if newRow - moveRow == destination[0] and newCol - moveCol == destination[1]:
                        return True
                    if (newRow - moveRow, newCol - moveCol) not in visited:
                        visited.add((newRow - moveRow, newCol - moveCol))
                        q.append([newRow - moveRow, newCol - moveCol])

        return False

