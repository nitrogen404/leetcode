""""
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays
"""

def arrayUnion(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] not in result:
            result.append(arr1[i])
            i += 1
        if arr2[j] not in result:
            result.append(arr2[j])
            j += 1
        i += 1
        j += 1
    if i < len(arr1):
        result.append(arr1[i])
        i += 1
    if j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result

print(arrayUnion([1, 2, 3, 4, 5], [1, 2, 3, 6 ,7]))

"""
Use two pointers to iterate over both arrays. 
While both pointers are less than the length of each array, check if the current element is not present in the result array, if not add it. 
Again for a final check, check if the the array length is still there in either of the array's and add the remaining elements. 
O(N) Time and O(N) space
"""