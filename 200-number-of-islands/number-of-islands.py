from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    queue = deque([(r, c)])
                    grid[r][c] = '0'
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in directions:
                            nRow, nCol = row + dr, col + dc
                            if 0 <= nRow < rows and 0 <= nCol < cols and grid[nRow][nCol] == '1':
                                grid[nRow][nCol] = '0'
                                queue.append((nRow, nCol))
        return islands

