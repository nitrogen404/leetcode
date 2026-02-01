class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right, k = 0, 1, 0
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            if right < len(nums):
                left += 1
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
                k += 1
        return k + 1