from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        initialColor = image[sr][sc]
        if initialColor == color:
            return image

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == initialColor:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        return image

