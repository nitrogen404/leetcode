class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == '0':
            return '0'
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                prod = digit1 * digit2

                p1 = i + j
                p2 = i + j + 1
                sum_ = prod + result[p2]
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10
            
        result_ = ''.join(map(str, result)).lstrip('0')
        return result_ or '0'