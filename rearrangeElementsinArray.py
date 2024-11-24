def rearrangeArray(nums):
    result = []
    negatives = []
    positives = []
    for i in nums:
        if i < 0:
            negatives.append(i)
        else:
            positives.append(i)
            
    for i in range(len(positives)):
        result.append(positives[i])
        result.append(negatives[i])
    return result




print(rearrangeArray([8, -9, 3, -2, 4, -7, 1, -6]))


        