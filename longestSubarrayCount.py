def subArraySum(nums, k):
    # prefixSum + currentSum = k
    prefixSum = 0
    map = {0: 1} # sum: count
    arrayCount = 0
    for i in nums:
        prefixSum += i
        if prefixSum - k in map:
            arrayCount += map[prefixSum - k]
        map[prefixSum] = map.get(prefixSum, 0) + 1
    return arrayCount




print(subArraySum([1,2,3], 3))
