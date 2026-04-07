class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a == parent_b:
            return False
        self.parents[parent_b] = parent_a
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        unionUtil = UnionFind(n)
        for x,y in edges:
            if not unionUtil.union(x,y):
                return False
        return True