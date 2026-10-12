from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {}
        indegree = [0] * numCourses
        for i in range(numCourses):
            graph[i] = []

        for course, preq in prerequisites:
            graph[preq].append(course)
            indegree[course] += 1
        
        q = deque()       
        for course in range(len(indegree)):
            if indegree[course] == 0:
                q.append(course)
        
        completed = 0
        while q:
            course = q.popleft()
            completed += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return completed == numCourses