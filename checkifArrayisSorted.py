# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
def checkSortedArray(nums):
    checkCounter = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i + 1) % len(nums)]:
            checkCounter += 1
        if checkCounter > 1:
            return True
    return False

print(checkSortedArray([4, 5, 1, 2, 3]))

