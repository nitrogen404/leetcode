from collections import deque
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        
        distance = [float('inf')] * n
        distance[0] = 0
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distance[neighbor] == float('inf'):
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        
        maxTime = 0
        for i in range(1, n):
            rtt = 2 * distance[i]
            if patience[i] >= rtt:
                lastReplyTime = rtt
            else:
                lastSent = ((rtt - 1) // patience[i]) * patience[i]
                lastReplyTime = lastSent + rtt
            maxTime = max(maxTime, lastReplyTime)
        return maxTime + 1