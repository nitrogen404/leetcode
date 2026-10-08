import heapq
import math
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        result = []

        for x, y in points:
            current_distance = x * x + y * y
            heapq.heappush(heap, [current_distance, x, y])

        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            result.append([x, y])
            
        return result