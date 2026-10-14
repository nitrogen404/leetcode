class Solution:
    def divide(self, divident: int, divisor: int) -> int:
        if divident == -2 ** 31 and divisor == -1: 
            return 2 ** 31 - 1
        
        if divident == divisor:
            return 1
        
        negative = False
        if divident < 0:
            negative = not negative
        if divisor < 0:
            negative = not negative
        
        divident, divisor = abs(divident), abs(divisor)
        quotient = 0
        while divident >= divisor:
            current_divisor = divisor
            multiple = 1
            while divident >= current_divisor + current_divisor:
                current_divisor += current_divisor
                multiple += multiple
            
            divident -= current_divisor
            quotient += multiple
        
        if negative:
            return -quotient
        return quotient
