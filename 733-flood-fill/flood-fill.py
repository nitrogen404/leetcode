from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows, cols = len(image), len(image[0])
        initial_color = image[sr][sc]
        if initial_color == color:
            return image
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([(sr, sc)])
        image[sr][sc] = color
        while q:
            row, col = q.popleft()
            for r, c in directions:
                nr, nc = row + r, col + c
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == initial_color:
                    image[nr][nc] = color
                    q.append((nr, nc))
                    
        return image
        