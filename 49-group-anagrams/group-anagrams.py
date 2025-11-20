class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in wordMap:
                wordMap[key] = []
            wordMap[key].append(word)
        return list(wordMap.values())