from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
        while q and fresh > 0:
            levelsize = len(q)
            for _ in range(levelsize):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1

        if fresh == 0:
            return time
        else:
            return -1        