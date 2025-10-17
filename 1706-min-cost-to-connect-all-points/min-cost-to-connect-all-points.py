import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        minHeap = [(0, 0)]
        totalcost = 0
        while len(visited) < n:
            cost, currentPoint = heapq.heappop(minHeap)
            if currentPoint in visited:
                continue
            visited.add(currentPoint)
            totalcost += cost
            for neighbor in range(n):
                if neighbor not in visited:
                    x1, y1 = points[currentPoint]
                    x2, y2 = points[neighbor]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (dist, neighbor))
        return totalcost