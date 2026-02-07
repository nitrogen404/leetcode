class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        windowSize = 2 * k + 1
        if windowSize > len(nums):
            return [-1] * len(nums)
        if k == 0:
            return nums
        
        result = [-1] * len(nums)
        currentSum = sum(nums[:windowSize])
        result[k] = currentSum // windowSize

        for i in range(k + 1, len(nums) - k):
            currentSum += nums[i + k] - nums[i - k - 1]
            result[i] = currentSum // windowSize
        return result