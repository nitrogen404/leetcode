from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        time = 0
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1


        
        while q and fresh > 0:
            level_size = len(q)
            for i in range(level_size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            time += 1

        if fresh == 0:
            return time
        else:
            return -1
