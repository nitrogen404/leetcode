import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        
        for i in range(k):
            result = -heapq.heappop(heap)
        return result