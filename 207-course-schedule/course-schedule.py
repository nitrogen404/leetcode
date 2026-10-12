from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for course, preq in prerequisites:
            adjList[preq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        completed = 0
        while q:
            node = q.popleft()
            completed += 1
            for neighbor in adjList[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return completed == numCourses
