class Solution:
    def decodeString(self, s: str) -> str:
        countStack, stringStack = [], []
        currentStr, num = '', 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                countStack.append(num)
                stringStack.append(currentStr)
                currentStr = ''
                num = 0
            elif ch == ']':
                repeatedTime = countStack.pop()
                prevStr = stringStack.pop()
                currentStr = prevStr + (currentStr * repeatedTime)
            else:
                currentStr += ch
        return currentStr