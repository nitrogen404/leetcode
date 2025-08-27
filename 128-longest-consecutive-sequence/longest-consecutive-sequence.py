class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums.sort()
        longest = 1
        currentLen = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                currentLen += 1
                longest = max(longest, currentLen)
            else:
                currentLen = 1
        return longest