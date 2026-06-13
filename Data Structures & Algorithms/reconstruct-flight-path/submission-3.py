class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s, d in tickets:
            adj[s].append(d)
        
        for k in adj:
            adj[k].sort()
        
        path = ["JFK"]

        def dfs(airport):
            if len(path) == len(tickets) + 1:
                return True
            if not adj[airport]:
                return False
            dest_list = adj[airport]
            for i, d in enumerate(dest_list):
                dest_list.pop(i)
                path.append(d)
                if dfs(d):
                    return True
                dest_list.insert(i, d)
                path.pop()
            return False
        dfs("JFK")
        return path