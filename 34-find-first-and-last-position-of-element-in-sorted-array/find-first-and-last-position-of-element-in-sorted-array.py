class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstOccurance = self.find_first_occurance(nums, target)
        lastOccurance = self.find_last_occurance(nums, target)
        return [firstOccurance, lastOccurance]
    
    def find_first_occurance(self, nums, target):
        l, h = 0, len(nums) - 1
        firstIndex = -1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                firstIndex = mid
                h = mid - 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return firstIndex
    
    def find_last_occurance(self, nums, target):
        l, h = 0, len(nums) - 1
        lastOccurance = -1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                lastOccurance = mid
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return lastOccurance
