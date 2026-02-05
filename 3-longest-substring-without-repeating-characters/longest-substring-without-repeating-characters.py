class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l, maxLen = 0, 0
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(hashmap[s[r]] + 1, l)
            hashmap[s[r]] = r
            currentLen = r - l + 1
            maxLen = max(maxLen, currentLen)
        return maxLen
            