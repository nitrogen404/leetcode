class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0] * len(isConnected)
        count = 0
        def dfs(node):
            nonlocal visited
            visited[node] = 1
            for neighbor in range(len(isConnected)):
                if not visited[neighbor] and isConnected[neighbor][node] == 1:
                    dfs(neighbor)
        
        for i in range(len(isConnected)):
            if visited[i] == 0:
                dfs(i)
                count += 1
        return count
