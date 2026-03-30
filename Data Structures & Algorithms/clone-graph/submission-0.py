"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}
        def dfs(node, hmap):
            if node and node not in hmap:
                copy_node = Node(node.val)
                hmap[node] = copy_node
            else:
                return hmap[node]
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor, hmap))
            return copy_node
        return dfs(node, hmap) if node else None

        