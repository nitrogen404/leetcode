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
        time = 0
        while heap or q:
            time += 1
            if q and q[0][1] <= time:
                task_freq, next_available_time = q.popleft()
                heapq.heappush(heap, (-task_freq))
            if heap:
                task_freq = -heapq.heappop(heap)
                task_freq -= 1
                if task_freq > 0:
                    next_available_time = n + 1 + time
                    q.append((task_freq, next_available_time))
        return time