"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""

def searchRange(nums, target):
    return [firstOccurance(nums, target), lastOccurance(nums, target)]

def firstOccurance(nums, target):
    first = -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid + 1
    return first

def lastOccurance(nums, target):
    last = -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid + 1
    return last


"""
The naive solution is to iterate over the array and find the first and the last occurance of an element or return -1, -1 if not found. This will require O(N) time complexity. 
We cannot perform binary search and find both first and last occurance of an element in array all at one time. SO we need to apply binary search twice, first to find first occurance and lastly to find the last occcurance. 

For the first occurance: 
if arr[mid] == target, we update the firstIndex to mid. Now for the first occurance definetly it will be on the left of mid as we need to find the first occurance. So we need to go to the left of mid. Hence we update high = mid - 1. This continues until low <= high. 

For last occurance:
it's the same but instead we move to the right of the mid to find the last occurance. 
"""