class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0
    
    # Find the root of node n
    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    # Determine if 2 nodes can be unioned:
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        res = []
        unionFind = UnionFind(n)
        for edge in edges:
            node1, node2 = edge
            if not unionFind.union(node1,node2):
                res.append(edge)
        return res[-1]
            
