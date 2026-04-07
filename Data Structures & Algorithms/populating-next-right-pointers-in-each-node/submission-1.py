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
        leftMost = root
        while leftMost.left:
            curr = leftMost
            while curr:
                curr.left.next = curr.right # perfect binary tree
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            leftMost = leftMost.left
        return root