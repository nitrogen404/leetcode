class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        maxLen, l = 0, 0
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(l, hashmap[s[r]] + 1)
            hashmap[s[r]] = r
            current_len = r - l + 1
            maxLen = max(current_len, maxLen)
        return maxLen