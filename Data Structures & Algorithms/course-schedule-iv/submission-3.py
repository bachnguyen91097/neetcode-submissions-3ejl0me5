class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_prereq = [[False] * numCourses for _ in range(numCourses)]

        adj = defaultdict(list)
        in_degree = defaultdict(int)
        for pre_course, course in prerequisites:
            adj[pre_course].append(course)
            in_degree[course] += 1
            is_prereq[pre_course][course] = True

        queue = deque()

        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        while queue:
            current_course = queue.popleft()
            for neighbor in adj[current_course]:
                for i in range(numCourses):
                    if is_prereq[i][current_course]:
                        is_prereq[i][neighbor] = True
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        res = []
        for course_1, course_2 in queries:
            res.append(is_prereq[course_1][course_2])

        return res