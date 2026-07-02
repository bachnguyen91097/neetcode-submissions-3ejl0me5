class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = defaultdict(int)

        for course, pre_course in prerequisites:
            adj[pre_course].append(course)
            in_degree[course] += 1
        
        queue = deque()
        visited = []

        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        while queue:
            current_course = queue.popleft()
            if current_course in visited:
                continue
            visited.append(current_course)
            for neighbor in adj[current_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return visited if len(visited) == numCourses else []