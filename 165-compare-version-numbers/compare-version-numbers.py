class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version_1 = list(map(int, version1.split('.')))
        version_2 = list(map(int, version2.split('.')))
        
        maxLen = max(len(version_1), len(version_2))
        while len(version_1) < maxLen:
            version_1.append(0)
        while len(version_2) < maxLen:
            version_2.append(0)
        
        for i in range(maxLen):
            if version_1[i] < version_2[i]:
                return -1
            elif version_1[i] > version_2[i]:
                return 1
        return 0