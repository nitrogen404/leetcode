class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        result = 0
        stack = []
        pse = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        
        stack = []
        nse = [len(nums)] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        
        for i in range(len(nums)):
            leftcount = i - pse[i]
            rightcount = nse[i] - i
            result = (result + nums[i] * leftcount * rightcount) % (10**9 + 7)
        return result

        