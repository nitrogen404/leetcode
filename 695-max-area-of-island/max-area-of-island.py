class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        max_area = 0
        def dfs(r, c):
            if (r >= rows or r < 0) or (c >= cols or c < 0):
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    area += dfs(nr, nc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area