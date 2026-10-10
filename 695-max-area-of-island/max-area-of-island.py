class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_area = 0

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            if (i, j) in visited:
                return 0

            visited.add((i, j))
            area = 1
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                area += dfs(nr, nc)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    current_area = dfs(i, j)
                    max_area = max(max_area, current_area)

        return max_area