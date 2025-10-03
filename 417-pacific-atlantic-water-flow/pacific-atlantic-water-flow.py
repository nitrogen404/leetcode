from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols  and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        pacificStarts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        pacificReach = bfs(pacificStarts)

        atlanticStarts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        atlanticReach = bfs(atlanticStarts)
        result = list(pacificReach & atlanticReach)
        return result
