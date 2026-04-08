from collections import defaultdict
from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)
        for prevCourse, nextCourse in relations:
            adj[nextCourse].append(prevCourse)

        visiting = set()
        memo = {}   # 👈 replace visited + res with memo

        def dfs(course):
            if course in visiting:
                return -1   # cycle
            if course in memo:
                return memo[course]

            visiting.add(course)

            max_depth = 1   # 👈 replaces current_semester list
            for neighbor in adj[course]:
                depth = dfs(neighbor)
                if depth == -1:
                    return -1
                max_depth = max(max_depth, depth + 1)

            visiting.remove(course)
            memo[course] = max_depth
            return max_depth

        ans = 0
        for course in range(1, n + 1):
            depth = dfs(course)
            if depth == -1:
                return -1
            ans = max(ans, depth)

        return ans