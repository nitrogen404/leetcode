class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory = {}
        maxLen, l = 0, 0
        for r in range(len(s)):
            if s[r] in memory and memory[s[r]] >= l:
                l = memory[s[r]] + 1

            memory[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
        return maxLen
        