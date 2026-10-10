class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # {
        #   0: [1, 2],
        #   1: [0, 2],
        #   2: [1, 0]
        # }
        visited = [False] * n
        def dfs(node):
            visited[node] = True
            if node == destination:
                return True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                
            return False
        return dfs(source)