class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(array, index):
            result.append(array[:])
            for i in range(index, len(nums)):
                if nums[i] != nums[i - 1] or index == i:
                    array.append(nums[i])
                    backtrack(array, i + 1)
                    array.pop()
        backtrack([], 0)
        return result