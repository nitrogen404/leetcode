import heapq
class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        
        sorted_queries = []
        for i in range(len(queries)):
            sorted_queries.append([queries[i], i])
        sorted_queries.sort()

        heap = []
        result = [-1] * len(queries)

        i = 0
        for query, original_index in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                interval_len = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, [interval_len, intervals[i][1]])
                i += 1
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            if heap:
                result[original_index] = heap[0][0]
        return result