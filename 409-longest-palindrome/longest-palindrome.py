class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = set()
        result = 0
        for char in s:
            if char not in frequency:
                frequency.add(char)
            else:
                frequency.remove(char)
                result += 2
        if frequency:
            return result + 1
        else:
            return result