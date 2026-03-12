class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        currentMax, maxSum = 0, float('-inf')
        currentMin, minSum = 0, float('inf')

        for num in nums:
            total += num
            currentMax = max(currentMax + num, num)
            maxSum = max(maxSum, currentMax)
            
            currentMin = min(currentMin + num, num)
            minSum = min(minSum, currentMin)

        if maxSum < 0:
            return maxSum
        return max(maxSum, total - minSum)