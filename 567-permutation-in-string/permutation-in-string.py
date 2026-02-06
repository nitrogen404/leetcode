class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        s1Counts = [0] * 26
        s2Counts = [0] * 26
        for i in range(l1):
            s1Counts[ord(s1[i]) - 97] += 1
            s2Counts[ord(s2[i]) - 97] += 1
        
        if s1Counts == s2Counts:
            return True
        
        for i in range(l1, l2): # (2, 8) - 2, 3, 4, 5, 6, 7
            s2Counts[ord(s2[i]) - 97] += 1
            s2Counts[ord(s2[i - l1]) - 97] -= 1
            if s1Counts == s2Counts:
                return True
        return False

        
