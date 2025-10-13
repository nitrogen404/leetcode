from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        queue = deque([(0, 0, 1)]) # (row, col, pathLength)
        visited = [[False]  * n for _ in range(n)]
        visited[0][0] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        while queue:
            row, col, length = queue.popleft()
            if row == n - 1 and col == n - 1:
                return length
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc, length + 1))
        return -1
