class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    perimeter += 4
                    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[dr + r][dc + c]:
                            perimeter -= 1
        return perimeter
