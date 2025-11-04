from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == '0':
            return "0"
        return ''.join(nums)