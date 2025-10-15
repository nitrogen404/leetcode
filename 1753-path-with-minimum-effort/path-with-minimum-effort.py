import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
        minHeap = [(0, 0, 0)] # effort, row, col
        while minHeap:
            currentEffort, r, c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return currentEffort
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    newEffort = max(diff, currentEffort)
                    if newEffort < effort[nr][nc]:
                        effort[nr][nc] = newEffort
                        heapq.heappush(minHeap, (newEffort, nr, nc))
        return -1


