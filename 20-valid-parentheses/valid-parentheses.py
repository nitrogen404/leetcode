class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if not stack:
                    return False

                top_char = stack.pop()
                if not ((char == ')' and top_char == '(') or
                        (char == ']' and top_char == '[') or
                        (char == '}' and top_char == '{')):
                    return False

        return len(stack) == 0