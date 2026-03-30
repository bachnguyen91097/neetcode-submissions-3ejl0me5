class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for p in prerequisites:
            pre_of_course, course = p
            adj[pre_of_course].append(course)
        
        visiting = set()
        visited = set()
        res = []

        def dfs(i, visiting, visited, adj):
            if i in visiting:
                return False
            if i in visited :
                return True
            visiting.add(i)
            for nei in adj[i]:
                if not dfs(nei, visiting, visited, adj):
                    return False
            visiting.remove(i)
            visited.add(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i, visiting, visited, adj):
                return False
        return True