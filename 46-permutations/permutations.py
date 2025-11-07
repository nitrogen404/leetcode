class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(array, used):
            if len(array) == len(nums):
                result.append(array[:])
                return 
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    array.append(nums[i])
                    backtrack(array, used)
                    array.pop()
                    used[i] = False
        backtrack([], [False] * len(nums))
        return result