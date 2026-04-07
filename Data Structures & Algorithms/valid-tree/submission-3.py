class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = defaultdict(list)
        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)
        def dfs(i, parent):
            visited.add(i)
            for neighbor in adj[i]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, i):
                    return False
            return True
        visited = set()
        dfs(0, -1)
        return len(visited) == n
        
        