from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    q = deque()
                    islands += 1
                    q.append((r, c))
                    grid[r][c] = '0'
                    while q:
                        row, col = q.popleft()
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                q.append((nr, nc))
                                grid[nr][nc] = '0'
        return islands
