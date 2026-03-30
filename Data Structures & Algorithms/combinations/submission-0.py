class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currComb = []
        res = []
        self.helper(1, currComb, res, n, k)
        return res
    
    def helper(self, i, currComb, res, n, k):
        if len(currComb) == k:
            res.append(currComb.copy())
            return
        if i > n:
            return
        
        for j in range(i, n+1):
            currComb.append(j)
            self.helper(j+1, currComb, res, n, k)
            currComb.pop()
