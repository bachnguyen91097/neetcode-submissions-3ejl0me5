class Union:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        parent_of_a = self.find(a)
        parent_of_b = self.find(b)
        if parent_of_a == parent_of_b:
            return False
        if self.rank[parent_of_a] < self.rank[parent_of_b]:
            self.parent[parent_of_a] = parent_of_b
        elif self.rank[parent_of_a] > self.rank[parent_of_b]:
            self.parent[parent_of_b] = parent_of_a
        else:
            self.parent[parent_of_a] = parent_of_b
            self.rank[parent_of_b] += 1
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        sorted_logs = sorted(logs, key=lambda log: log[0])
        group_count = n
        union = Union(n)
        for timestamp, a, b in sorted_logs:
            if union.union(a,b):
                group_count -= 1
            if group_count == 1:
                return timestamp
        return -1