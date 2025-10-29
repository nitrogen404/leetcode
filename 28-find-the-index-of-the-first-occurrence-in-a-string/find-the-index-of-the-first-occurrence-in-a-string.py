class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            j = 0
            for k in range(i, len(haystack)):
                if haystack[k] == needle[j]:
                    j += 1
                else:
                    break
                if j == len(needle):
                    return i
        return -1