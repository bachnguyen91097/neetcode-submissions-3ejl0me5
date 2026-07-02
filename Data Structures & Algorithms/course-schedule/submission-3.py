class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = defaultdict(int)

        for course, pre_course in prerequisites:
            in_degree[course] += 1
            adj[pre_course].append(course)
        
        queue = deque()
        visited = set()

        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        while queue:
            current_course = queue.popleft()
            if current_course in visited:
                continue
            visited.add(current_course)
            for neighbor in adj[current_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(visited) == numCourses