def pairWithMaxSum(arr):
        # Your code goes here
        scr = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                tempScr = 0
                subArr = arr[i: j + 1]
                smallest = min(subArr)
                secondSmallest = 100000000000000000
                largest = max(subArr)
                for j in range(len(subArr)):
                    if subArr[j] > smallest:
                        if subArr[j] < largest and subArr[j] < secondSmallest:
                            secondSmallest = subArr[j]
                tempScr = secondSmallest + smallest
                scr = max(tempScr, scr)
        return scr

print(pairWithMaxSum([4, 3, 1, 5, 6]))