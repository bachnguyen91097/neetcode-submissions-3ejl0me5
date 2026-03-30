class UnionJoin():
    def __init__(self,small, big):
        self.parent = {}
        self.rank = {}

        for i in range(small, big + 1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

        return True 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        minNum = min(nums)
        maxNum = max(nums)

        if minNum == maxNum:
            return 1

        union = UnionJoin(minNum, maxNum)
        for i in range(minNum, maxNum):
            for j in range(minNum + 1, maxNum + 1):
                if i in nums and j in nums:
                    union.union(i, j)
        
        res = 1
        maxRes = float("-inf")
        for i in range(minNum + 1,maxNum+1):
            if union.parent[i-1] == union.parent[i]:
                res += 1
                maxRes = max(res, maxRes)
            else:
                res = 1
        return maxRes
        