def floorInSortedArray(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] <= k:
            return mid
        elif nums[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return -1



print(floorInSortedArray([1,2,8,10,11,12,19], 0))

