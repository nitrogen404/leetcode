from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([(sr, sc)])
        initial_color = image[sr][sc]
        
        if initial_color == color:
            return image
        
        image[sr][sc] = color

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == initial_color:
                    q.append((nr, nc))
                    image[nr][nc] = color
        return image