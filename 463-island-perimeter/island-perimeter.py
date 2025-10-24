from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visited.add((r, c))
                    break
            if queue:
                break
        
        perimeter = 0
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                    perimeter += 1
                elif (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return perimeter


        
        
