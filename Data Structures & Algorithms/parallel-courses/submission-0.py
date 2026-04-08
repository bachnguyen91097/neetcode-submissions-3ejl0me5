class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)
        for relation in relations:
            prevCourse, nextCourse = relation
            adj[nextCourse].append(prevCourse)
        visiting = set()
        visited = set()
        res = []
        def dfs(course, adj, visiting, visited):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            current_semester = []
            for neighbor in adj[course]:
                if not dfs(neighbor, adj, visiting, visited):
                    return False
                current_semester.append(neighbor)
            visiting.remove(course)
            visited.add(course)
            if current_semester:
                res.append(current_semester)  
            return True
        for course in range(1, n+1):
            if not dfs(course, adj, visiting, visited):
                return -1
        print(res)
        return len(res) + 1
                
        