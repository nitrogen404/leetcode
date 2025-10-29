class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prevVal = 0
        i = len(s) - 1
        while i >= 0:
            currentVal = hashmap[s[i]]
            if currentVal < prevVal:
                result -= currentVal
            else:
                result += currentVal
            prevVal = currentVal
            i -= 1
        return result
            