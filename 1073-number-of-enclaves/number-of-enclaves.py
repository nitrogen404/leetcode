class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            if grid[i][j] == 0:
                return

            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Left and right borders
        for r in range(rows):
            if grid[r][0] == 1:
                dfs(r, 0)

            if grid[r][cols - 1] == 1:
                dfs(r, cols - 1)

        # Top and bottom borders
        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0, c)

            if grid[rows - 1][c] == 1:
                dfs(rows - 1, c)

        moves = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    moves += 1

        return moves