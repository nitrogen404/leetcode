from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque([source])
        visited = set()
        while q:
            node = q.popleft()
            visited.add(node)
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return False

