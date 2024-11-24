# https://www.geeksforgeeks.org/problems/rotation4723/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotation

def findMinimum(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]


print(findMinimum([3,4,5,1,2]))


"""
if nums[mid] > nums[high], then the minimum element would be in the right part of the array or it could also be at nums[mid], so we set low = mid + 1 to eliminate left half
else we eliminate left half 
"""