class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        l = 0
        currentSum = 0
        for r in range(len(nums)):
            currentSum += nums[r]
            while currentSum >= target:
                minLen = min(minLen, r - l + 1)
                currentSum -= nums[l]
                l += 1
        return minLen if minLen != float('inf') else 0