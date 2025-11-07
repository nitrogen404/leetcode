class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.result = []
        map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

        def backtrack(s, index):
            if len(s) == len(digits):
                self.result.append(s)
                return 
            for char in map[digits[index]]:
                backtrack(s + char, index + 1)
        
        backtrack("", 0)
        return self.result