class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        matrix = [[-1] * numCourses for _ in range(numCourses)]

        for preCourse, course in prerequisites:
            adj[course].append(preCourse)
            matrix[course][preCourse] = 1
        def dfs(preCourse, course):
            if matrix[course][preCourse] != -1:
                return matrix[course][preCourse] == 1
            for nei in adj[course]:
                if nei == preCourse or dfs(preCourse, nei):
                    matrix[course][preCourse] = 1
                    return True
            matrix[course][preCourse] = 0
            return False
        res = []
        for u,v in queries:
            res.append(dfs(u,v))
        return res