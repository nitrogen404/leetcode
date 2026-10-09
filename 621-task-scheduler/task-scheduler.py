from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequency = {}
        for task in tasks:
            if task not in frequency:
                frequency[task] = 0
            frequency[task] += 1
        
        max_heap = []
        q = deque()
        for task in frequency:
            heapq.heappush(max_heap, -frequency[task])
        
        time = 0
        while max_heap or q:
            time += 1
            if q and q[0][1] <= time:
                count, available_time = q.popleft()
                heapq.heappush(max_heap, -count)
            if max_heap:
                count = -heapq.heappop(max_heap)
                count -= 1
                if count > 0:
                    available_time = time + n + 1
                    q.append((count, available_time))
        return time

