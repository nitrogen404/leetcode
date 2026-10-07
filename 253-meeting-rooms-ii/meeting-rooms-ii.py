import heapq
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        heap = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)