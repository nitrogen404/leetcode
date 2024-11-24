def findKthRotation(nums):
    k = 0
    for i in range(len(nums) -1):
        if nums[i] > nums[(i + 1) % len(nums)]:
            k += 1
    return k

print(findKthRotation([1, 2, 3, 4]))

