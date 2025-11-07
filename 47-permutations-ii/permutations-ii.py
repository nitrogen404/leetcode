class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(array, used):
            if len(array) == len(nums):
                result.append(array[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                array.append(nums[i])
                backtrack(array, used)
                array.pop()
                used[i] = False
        backtrack([], [False] * len(nums))
        return result