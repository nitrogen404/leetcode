import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 0
            freq[task] += 1
        
        heap = []
        for task in freq:
            heapq.heappush(heap, -freq[task])
        
        q = deque()

        interval = 0
        while heap or q:
            interval += 1
            if q and q[0][1] <= interval:
                count, next_available_time = q.popleft()
                heapq.heappush(heap, -count)
            if heap:
                count = -heapq.heappop(heap)
                count -= 1
                if count > 0:
                    next_available_time = interval + 1 + n
                    q.append((count, next_available_time))

        return interval
