class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        def dfs(current, target, visited):
            if current == target:
                return True
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False
        
        for u, v in edges:
            if u in graph and v in graph:
                if dfs(u, v, set()):
                    return [u, v]
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)            

