class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        max_len, l = 0, 0
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(hashmap[s[r]] + 1, l)
            hashmap[s[r]] = r
            current_len = r - l + 1
            max_len = max(max_len, current_len)
        return max_len            
            