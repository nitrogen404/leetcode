from collections import deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        windowcount = {}
        l, r, formed, minLen = 0, 0, 0, float('inf')
        ans = (0, 0)
        while r < len(s):
            c = s[r]
            windowcount[c] = windowcount.get(c, 0) + 1
            if c in need and windowcount[c] == need[c]:
                formed += 1
            while l <= r and formed == len(need):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    ans = (l, r)
                charLeft = s[l]
                windowcount[charLeft] -= 1
                if charLeft in need and windowcount[charLeft] < need[charLeft]:
                    formed -= 1
                l += 1
            r += 1
        l, r = ans
        return s[l: r + 1] if minLen != float('inf') else ""
