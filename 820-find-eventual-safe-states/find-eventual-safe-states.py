class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        state = [0] * len(graph)
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1
            for neighbors in graph[node]:
                if not dfs(neighbors):
                    return False
            state[node] = 2
            return True
        result = []
        for i in range(len(graph)):
            if dfs(i):
                result.append(i)
        return result