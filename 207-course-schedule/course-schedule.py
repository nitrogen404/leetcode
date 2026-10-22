from collections import deque
class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courses = prerequisites
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        indegree = [0] * numCourses

        for course, preq in courses:
            adj[preq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        completed = 0
        while q:
            course = q.popleft()
            completed += 1

            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return completed == numCourses