import math
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        memo = {1: k, 2: k*k}
        for i in range(3, n+1):
            memo[i] = (k - 1) * (memo[i-1] + memo[i-2])
        return memo[n]
