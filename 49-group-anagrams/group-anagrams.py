class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyMap = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in keyMap:
                keyMap[key] = []
            keyMap[key].append(word)
        return list(keyMap.values())