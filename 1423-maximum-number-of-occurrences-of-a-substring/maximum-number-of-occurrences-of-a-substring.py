class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        subStringCount = {}
        charFreq = {}
        maxOcc = 0
        l = 0

        for r in range(len(s)):
            charFreq[s[r]] = charFreq.get(s[r], 0) + 1
            if r - l + 1 > minSize:
                charFreq[s[l]] -= 1
                if charFreq[s[l]] == 0:
                    del charFreq[s[l]]
                l += 1
            if r - l + 1 == minSize:
                if len(charFreq) <= maxLetters:
                    subStr = s[l: r + 1]
                    subStringCount[subStr] = subStringCount.get(subStr, 0) + 1
                    maxOcc = max(maxOcc, subStringCount[subStr])
        return maxOcc