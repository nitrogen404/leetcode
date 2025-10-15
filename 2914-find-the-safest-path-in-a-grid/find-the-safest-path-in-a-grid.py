import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        safeness = [[-1] * n for _ in range(n)]
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    safeness[r][c] = 0
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and safeness[nr][nc] == -1:
                    safeness[nr][nc] = safeness[r][c] + 1
                    queue.append((nr, nc))

        maxHeap = [(-safeness[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        while maxHeap:
            s, r, c = heapq.heappop(maxHeap)
            s = -s
            if r == n - 1 and c == n - 1:
                return s
            if visited[r][c]: 
                continue
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    minSafeness = min(safeness[nr][nc], s)
                    heapq.heappush(maxHeap, (-minSafeness, nr, nc))
        return -1
