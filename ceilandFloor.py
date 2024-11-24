"""

"""

def getFloorandCeil(array, x):
    ceil, floor = -1, -1
    for i in array:
        if i <= x:
            if i > floor:
                floor = i
        if i >= x:
            if i < ceil or ceil == -1:
                ceil = i
            
    return [floor, ceil]


def ceilAndFloorSorted(array, k):
    floor, ceiling = -1, -1
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == k:
            return [array[mid], array[mid]]
        elif k < array[mid]:
            ceiling = array[mid]
            high = mid - 1
        else:
            floor = array[mid]
            low = mid + 1
    return [floor, ceiling]  
print(getFloorandCeil([9, 98], 64))