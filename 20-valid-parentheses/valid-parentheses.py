class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if not stack: 
                    return False
                
                prev = stack.pop()
                if not ((prev == '(' and ch == ')') or (prev == '{' and ch == '}') or (prev == '[' and ch == ']')):

                        return False
        return len(stack) == 0
                         