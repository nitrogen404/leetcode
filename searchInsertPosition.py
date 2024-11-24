"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""
def searchInsert(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return low

print(searchInsert([1, 3, 5, 6, 8, 10, 12, 15], 7))

"""
implement binary search.
At a point when low == high, low will be at the position where the target has to be inserted.
Time complexity O(logn)  
"""