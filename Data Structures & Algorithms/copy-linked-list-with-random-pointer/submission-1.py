"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copyCurr = old_to_new[curr]
            copyCurr.next = old_to_new.get(curr.next)
            copyCurr.random = old_to_new.get(curr.random)
            curr = curr.next
        return old_to_new[head] if head else None
        