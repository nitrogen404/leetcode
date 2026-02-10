class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        for i in range(2 * len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i % len(nums)]:
                stack.pop()
            if i < len(nums):
                if stack:
                    result[i] = stack[-1]
            stack.append(nums[i % len(nums)])
        return result