class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []

        def dfs(i):
            if i == len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return res