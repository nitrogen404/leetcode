class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        deapth = 0
        for char in s:
            if char == '(':
                if deapth > 0:
                    result.append(char)
                deapth += 1
            else:
                deapth -= 1
                if deapth > 0:
                    result.append(char)
        return ''.join(result)

                    