"""
Given an integer n, find the square root of n. If n is not a perfect square, then return the floor value.

Floor value of any number is the greatest Integer which is less than or equal to that number. 
Solve this in O(logN) time. 
"""

def sqrtofNum(n):
    i = 1
    while i * i <= n:
        i += 1
    return i - 1

def squareroot(n):
    array = [i for i in range(1, n + 1)]
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] * array[mid] <= n:
            low = mid + 1
        else:
            high = mid - 1
    return array[high]

print(squareroot(10))