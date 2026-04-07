"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            queue_length = len(queue)
            current_level = []
            for i in range(queue_length):
                element = queue.popleft()
                current_level.append(element)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            for i in range(len(current_level)-1):
                current_level[i].next = current_level[i+1]
            current_level[-1].next = None
        return root
