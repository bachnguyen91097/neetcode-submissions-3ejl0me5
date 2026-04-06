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
        copyHead = copy.deepcopy(head)
        return copyHead
        # curr = head
        # hmap = {head: copyHead}
        # while curr:
        #     nextNode = curr.next
        #     nextNodeCopy = copy.deepcopy(nextNode)
        #     hmap[nextNode] = nextNodeCopy
        #     curr = nextNode
        