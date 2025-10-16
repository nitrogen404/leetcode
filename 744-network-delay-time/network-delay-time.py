import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for src, dst, time in times:
            if src not in graph:
                graph[src] = []
            graph[src].append((dst, time))
        
        heap = [(0, k)]
        visited = set()
        minTime = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            minTime = max(time, minTime)
            for neighbor, w in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(heap, (time + w, neighbor))
        return minTime if len(visited) == n else -1
            
            


