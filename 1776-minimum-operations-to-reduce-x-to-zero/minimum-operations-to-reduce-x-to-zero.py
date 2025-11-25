class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        l = 0
        currentSum = 0
        maxLen = -1
        for r in range(len(nums)):
            currentSum += nums[r]
            while currentSum > target and l <= r:
                currentSum -= nums[l]
                l += 1

            if currentSum == target:
                maxLen = max(maxLen, r - l + 1)
        return len(nums) - maxLen if maxLen != -1 else -1 

        