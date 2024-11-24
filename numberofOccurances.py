"""
Given a sorted array, arr and a number target, you need to find the number of occurrences of target in arr
"""

def numberofOccurances(nums, target):
    firstIndex = firstOccurance(nums, target)
    lastIndex = lastOccurance(nums, target)
    if firstIndex == -1 or lastIndex == -1:
        return 0
    else:
        return lastIndex - firstIndex + 1
        

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
            high = mid - 1
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
            high = mid - 1
    return last

print(numberofOccurances([1, 1, 2, 2, 2, 2, 3], 3))
