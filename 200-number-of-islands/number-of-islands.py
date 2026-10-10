from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    islands += 1
                    queue = deque([(r, c)])
                    grid[r][c] = '0'
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in direction:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                queue.append((nr, nc))

        return islands

                