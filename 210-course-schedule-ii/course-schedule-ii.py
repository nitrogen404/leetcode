from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = {}
        result = []

        for i in range(numCourses):
            graph[i] = []
        
        indegree = [0] * numCourses
        for course, preq in prerequisites:
            graph[preq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            result.append(course)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return result if len(result) == numCourses else []
