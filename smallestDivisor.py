# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
import math
def smallestDivisor(nums, threshold):
    low, high = 0, max(nums) # or any large number like 10 ** 12
    while low <= high:
        mid = (low + high) // 2
        if checkResult(nums, mid, threshold):
            high = mid - 1
        else:
            low = mid + 1
    return low

def checkResult(nums, divisor, threshold):
    Sum = 0
    for i in nums:
        Sum += math.ceil(i / divisor)
    return Sum <= threshold


"""
Apply binary search on range of integers from 1 to largest int (max(array) or 10**12). if with any certain divisor the Sum <= threshold, then we need to check for the minimum integer for which Sum <= threshold. So we eliminate right part of that divisor. ie high = mid - 1
else: low = mid + 1. 
Time complexity O(MLogn) where M is the length of nums. 
"""