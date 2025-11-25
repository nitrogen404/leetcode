from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minDeque = deque()
        maxDeque = deque()
        l = 0
        result = 0
        for r in range(len(nums)):
            while maxDeque and maxDeque[-1] < nums[r]:
                maxDeque.pop()
            maxDeque.append(nums[r])

            while minDeque and minDeque[-1] > nums[r]:
                minDeque.pop()
            minDeque.append(nums[r])

            while maxDeque[0] - minDeque[0] > limit:
                if nums[l] == maxDeque[0]:
                    maxDeque.popleft()
                if nums[l] == minDeque[0]:
                    minDeque.popleft()
                l += 1

            result = max(r - l + 1, result)
        return result