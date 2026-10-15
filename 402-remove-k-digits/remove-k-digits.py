class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for r in num:
            while stack and k > 0 and stack[-1] > r:
                    stack.pop()
                    k -= 1
            stack.append(r)
        
        while k > 0:
            stack.pop()
            k -= 1
        result = ''.join(stack).lstrip('0')
        if result == '':
            return '0'
        return result
        
