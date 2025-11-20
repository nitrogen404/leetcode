from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        freqS = Counter()
        freqP = Counter(p)
        k = len(p)
        for i in range(len(s)):
            freqS[s[i]] += 1
            if i >= k:
                if freqS[s[i - k]] == 1:
                    del freqS[s[i - k]]
                else:
                    freqS[s[i - k]] -= 1
            if freqS == freqP:
                result.append(i - k + 1)
        return result    