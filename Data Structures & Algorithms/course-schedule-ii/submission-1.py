class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for n in range(numCourses):
            adj[n] = []
        for course,pre_course in prerequisites:
            adj[course].append(pre_course)
        visiting = set()
        visited = []
        def dfs(i, adj, visiting, visited):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for neighbor in adj[i]:
                if not dfs(neighbor, adj, visiting, visited):
                    return False
            visiting.remove(i)
            visited.append(i)
            return True
        for course in range(numCourses):
            dfs(course, adj, visiting, visited)
        return visited if len(visited) == numCourses else []
