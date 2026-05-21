class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            ways = dfs(i+1)
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
            cache[i] = ways
            return ways
        return dfs(0)
        