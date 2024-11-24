"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

def maxSubArray(nums):
    maxSum = nums[0]
    currentSum = 0
    for i in nums:
        currentSum += i
        maxSum = max(maxSum, currentSum)
        if currentSum < 0: currentSum = 0
    return maxSum


""""
in problems with finding maximum sum in a subarray use Kadane's algorithm. 
"""