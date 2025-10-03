from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        freshOranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    freshOranges += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        timeElapsed = 0
        while queue:
            row, col, time = queue.popleft()
            timeElapsed = max(timeElapsed, time)
            for dr, dc in directions:
                nRow, nCol = row + dr, col + dc
                if 0 <= nRow < rows and 0 <= nCol < cols and grid[nRow][nCol] == 1:
                    grid[nRow][nCol] = 2
                    freshOranges -= 1
                    queue.append((nRow, nCol, time + 1))
        return timeElapsed if freshOranges == 0 else -1