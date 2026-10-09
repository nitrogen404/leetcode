import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
 
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        largest_left = -heapq.heappop(self.left)
        heapq.heappush(self.right, largest_left)
        if len(self.right) > len(self.left):
            smallest_right = heapq.heappop(self.right)
            heapq.heappush(self.left, -smallest_right)

            
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        
        left_max = -self.left[0]
        right_min = self.right[0]
        return (left_max + right_min) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()