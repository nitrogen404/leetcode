"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
"""

def singleElementinSortedArray(nums):
    result = 0
    for i in nums:
        result ^= i
    return result

def singleElementBinarySearch(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if mid % 2 == 0:
            if nums[mid] != nums[mid + 1]:
                high = mid
            else:
                low = mid + 2
        else:
            if nums[mid] == nums[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
    return nums[low]

"""
To find the single element occuring in an array using binary search. THE MOST IMPORTANT CONDITION IS THAT THE ARAY SHOULD BE SORTED. IF the array isn't sorted then XORing works in linear time, but if the array is sorted then using binary search the problem can be solved more efficiently in O(logn) time. 

** if all the elements occur twice, then a pair starts on even index and ends at odd index. If this pattern is disturbed then there's an element that occurs only once. 

If mid == even, then arr[mid] == arr[mid + 1]. IF this is not met, then the singlemost element will definetly be on the LEFT side. So left = mid + 2, else high = mid

if mid == odd, then arr[mid] == arr[mid - 1]. IF this is not met, then singlemost element is on left side else, on right side. So high = mid - 1, else low = mid + 1
"""
