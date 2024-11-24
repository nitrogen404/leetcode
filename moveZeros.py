"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Do it with inplace solution.
"""
def moveZeroes(nums):
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1

print(moveZeroes([0,1,0,3,12]))

"""
Start with a pointer left at index 0. 
HAve another pointer that also starts from index 0. 
Swap it with left if nums[right] != 0, increment left.
O(N) time, O(1) space
"""