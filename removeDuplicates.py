"""
Given a sorted integer array 'nums', remove the duplicates in-place 
so that each unique element appears only once. The order of elements 
should be maintained as they originally appeared.

The result should be:
1. The first 'k' elements in the array should contain the unique elements.
2. The remaining elements are not important.
3. Return 'k', which is the number of unique elements in 'nums'.

The solution should be done in O(n) time and O(1) extra space.
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

def removeDuplicates(nums):
        j = 1
        i = 0
        k = 0
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                k += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        return k + 1


"""

Use two pointers i and j, increment j in every case and i only when nums[j] != nums[i]. Return k + 1 at the end

"""