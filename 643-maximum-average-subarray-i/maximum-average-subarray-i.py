class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        maxSum = windowSum
        for r in range(k, len(nums)):
            windowSum += nums[r] - nums[r - k]
            maxSum = max(windowSum, maxSum)
        return maxSum / k
