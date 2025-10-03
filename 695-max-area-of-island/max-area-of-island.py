from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    grid[r][c] = 0
                    queue = deque([(r, c)])
                    while queue:
                        row, col = queue.popleft()
                        area += 1
                        for dr, dc in directions:
                            nRow, nCol = row + dr, col + dc
                            if 0 <= nRow < rows and 0 <= nCol < cols and grid[nRow][nCol] == 1:
                                grid[nRow][nCol] = 0
                                queue.append((nRow, nCol))
                    maxArea = max(maxArea, area)
        return maxArea
