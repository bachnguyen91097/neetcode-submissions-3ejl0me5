class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # do the heirhomzer algo way
        adj = defaultdict(list)
        out_degree = defaultdict(int)
        in_degree = defaultdict(int)

        for source, dest in tickets:
            adj[source].append(dest)
            out_degree[source] += 1
            in_degree[dest] += 1
        
        starting = 'JFK'

        path = []

        def dfs(node):
            while adj[node]:
                dest_list = adj[node]
                dest_list.sort(reverse=True)
                next_node = dest_list.pop()
                dfs(next_node)
            path.append(node)
        
        dfs(starting)
        return path[::-1]