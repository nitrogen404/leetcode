class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    lastChar = stack.pop()
                    if not ((s[i] == '}' and lastChar == '{') or 
                    (s[i] == ']' and lastChar == '[') or 
                    (s[i] == ')' and lastChar == '(')):
                        return False
        return len(stack) == 0
          
