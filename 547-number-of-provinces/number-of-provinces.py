class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0] * len(isConnected)
        
        def dfs(city):
            visited[city] = 1
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        provinces = 0
        for city in range(len(isConnected)):
            if not visited[city]:
                provinces += 1
                dfs(city)
        return provinces