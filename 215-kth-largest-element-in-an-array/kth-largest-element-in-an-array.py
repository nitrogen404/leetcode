import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        result = 0
        for i in range(k):
            result = -heapq.heappop(max_heap)
        return result
