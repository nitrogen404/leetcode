class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        shapes = set()
        def dfs(r, c, base_r, base_c, shape):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            
            if grid[r][c] == 0:
                return 
            
            grid[r][c] = 0
            shape.append((r - base_r, c - base_c))

            dfs(r + 1, c, base_r, base_c, shape)
            dfs(r - 1, c, base_r, base_c, shape)
            dfs(r, c + 1, base_r, base_c, shape)
            dfs(r, c - 1, base_r, base_c, shape)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    shape = []
                    dfs(r, c, r, c, shape)
                    shapes.add(tuple(shape))
        return len(shapes)