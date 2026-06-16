class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # do the heirhomzer algo way
        adj = defaultdict(list)

        for source, dest in tickets:
            adj[source].append(dest)
        
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