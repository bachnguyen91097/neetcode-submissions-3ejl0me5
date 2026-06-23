from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        q = deque()
        visited = set(deadends)
        
        def children(lock):
            res = []
            for i in range(4):
                forward = (int(lock[i]) + 1) % 10
                res.append(lock[:i] + str(forward) + lock[i+1:])
                backward = (int(lock[i]) - 1 + 10) % 10
                res.append(lock[:i] + str(backward) + lock[i+1:])
            return res

        q.append(('0000', 0))
        while q:
            lock, turn = q.popleft()
            if lock == target:
                return turn
            
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turn + 1))
        
        return -1