def longestSubArraySum(nums):
    maxSum = 0
    longestArray = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            tempArray = nums[i: j + 1]
            if sum(tempArray) > maxSum:
                maxSum = sum(tempArray)
                longestArray = tempArray
    return longestArray

print(longestSubArraySum([-2,1,-3,4,-1,2,1,-5,4]))
