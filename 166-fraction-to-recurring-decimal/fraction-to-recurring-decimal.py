class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)

        intPart = numerator // denominator
        result.append(str(intPart))
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(result)
        result.append(".")
        remainderMap = {}
        while remainder != 0:
            if remainder in remainderMap:
                index = remainderMap[remainder]
                result.insert(index, "(")
                result.append(")")
                break
            remainderMap[remainder] = len(result)
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder = remainder % denominator
        return ''.join(result)
