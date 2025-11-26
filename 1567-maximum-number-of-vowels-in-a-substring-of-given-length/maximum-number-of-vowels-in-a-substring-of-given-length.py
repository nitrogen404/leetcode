class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = 0
        maxVovels = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxVovels = count
        for r in range(k, len(s)):
            if s[r] in vowels:
                count += 1
            if s[r - k] in vowels:
                count -= 1
            maxVovels = max(maxVovels, count)
        return maxVovels