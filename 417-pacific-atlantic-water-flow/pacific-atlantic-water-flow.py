from collections import deque
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        
        def bfs(start):
            visited = set(start)
            q = deque(start)
            while q:
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited
        
        pacific_start = []
        for c in range(cols):
            pacific_start.append((0, c))

        for r in range(rows):
            pacific_start.append((r, 0))

        
        atlantic_start = []
        for c in range(cols):
            atlantic_start.append((rows - 1, c))

        for r in range(rows):
            atlantic_start.append((r, cols - 1))


        pacific_points = bfs(pacific_start)
        atlantic_points = bfs(atlantic_start)
        common = pacific_points & atlantic_points
        
        result = []
        for r, c in common:
            result.append([r, c])
        
        return result