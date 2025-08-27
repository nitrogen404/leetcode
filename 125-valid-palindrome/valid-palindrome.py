class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = self.cleanStr(s)
        left, right = 0, len(cleanString) - 1
        while left <= right:
            if cleanString[left].lower() != cleanString[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def cleanStr(self, s):
        return ' '.join(char for char in s if char.isalnum())