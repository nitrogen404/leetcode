class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        minimum_element = float('inf')

        while l <= h:
            mid = (l + h) // 2
            if nums[l] <= nums[h]:
                minimum_element = min(minimum_element, nums[l])
                break
            
            if nums[l] <= nums[mid]:
                minimum_element = min(minimum_element, nums[l])
                l = mid + 1
            
            else:
                minimum_element = min(minimum_element, nums[mid])
                h = mid - 1
        return minimum_element

