class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        freq_map = {}
        max_freq = 0
        l, result = 0, 0
        
        for r in range(len(nums)):
            freq_map[nums[r]] = freq_map.get(nums[r], 0) + 1
            max_freq = max(max_freq, freq_map[nums[r]])
            
            while (r - l + 1) - max_freq > k:
                freq_map[nums[l]] -= 1
                l += 1
            
            result = max(result, max_freq)
        return result