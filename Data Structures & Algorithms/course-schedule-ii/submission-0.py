class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for p in prerequisites:
            c, pre_c = p
            adj[pre_c].append(c)
        
        visiting = set()
        visited = set()
        res = []

        def dfs(course, adj, visiting, visited, res):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for pre_course in adj[course]:
                if not dfs(pre_course, adj, visiting, visited, res):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i, adj, visiting, visited, res):
                return []

        res.reverse()
        return res