class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            current_sum = nums_with_index[l][0] + nums_with_index[r][0]
            if current_sum == target:
                return [nums_with_index[l][1], nums_with_index[r][1]]
            elif current_sum > target:
                r -= 1
            else:
                l += 1
        return []
        
        
                