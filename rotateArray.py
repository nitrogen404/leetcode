"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
"""

def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l = 0 
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l = 0 
        r = k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l = k 
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


def rotateArr(nums, k):
    resultArr = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        newIdx = (i + k) % len(nums)
        resultArr[newIdx] = nums[i]
    return resultArr

print(rotateArr([1,2,3,4,5,6,7], 8))

"""
the equation k = k % len(nums) or k = (i + k) % len(nums) works because we are wrapping the out of bounds index within the range of len(nums)

Rotating an array of len(n) by multiples of n will result in the same array. IF k is greater than len(nums) rotating the array by more than its length is unnecessary. Rotating an array of len 7 by 10 positions results in the same outcome as rotating it by 3 position 
hence k = k % len(nums) k = 3 % 7 = 3  && k = 10 % 8 = 3


O(1) memory and O(n) time
Step 1: reverse the entire array by two pointers
Step 2: reverse the elements from 0 to k 
Step 3: reverse the elements from k to len(nums) - 1 
"""