class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        prefixLength = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                prefixLength = i
        return prefixLength