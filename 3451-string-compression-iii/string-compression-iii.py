class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        l = 0
        while l < len(word):
            r = l
            while r < len(word) and word[r] == word[l]:
                r += 1
            
            count = r - l
            char = word[l]
            while count > 0:
                take = min(9, count)
                res.append(str(take) + char)
                count -= take
            
            l = r
        return ''.join(res)
