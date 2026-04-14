class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        hashmap = {}
        max_freq = 0
        l, result = 0, 0
        for r in range(len(nums)):
            hashmap[nums[r]] = hashmap.get(nums[r], 0) + 1
            max_freq = max(max_freq, hashmap[nums[r]])
            while (r - l + 1) - max_freq > k:
                hashmap[nums[l]] -= 1
                l += 1
            result = max(result, max_freq)
        return result