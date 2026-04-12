class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            src, dst = equations[i]
            graph[src].append([dst, values[i]])
            graph[dst].append([src, 1/values[i]])
        res = []

        def dfs(src, dst, graph, visited):
            if src in visited:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for neighbor, weight in graph[src]:
                result = dfs(neighbor, dst, graph, visited)
                if result != -1.0:
                    return result * weight
            return -1.0

        for src, dst in queries:
            if src not in graph or dst not in graph:
                res.append(-1.0)
            elif src == dst:
                res.append(1.0)
            else:
                visited = set()
                res.append(dfs(src, dst, graph, visited))
        
        return res