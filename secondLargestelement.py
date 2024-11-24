"""
Given an array arr of all positive elements, return the second largest distinct element from an array without sorting. If the second largest element doesn't exist then return -1

"""

def  secondLargestElement(array):
    largest = array[0]
    secondLargest = -1 
    for i in range(1, len(array)):
        if array[i] > largest:
            secondLargest = largest
            largest = array[i]
        elif array[i] < largest and secondLargest < array[i]:
            secondLargest = array[i]
    return secondLargest


print(secondLargestElement([12, 35, 1, 10, 34, 1]))


"""
Assuming all the numbers are positive, we set secondLargest as -1, if not then we'll set it some very negative value. 
We assume that the largest element is the first element and secondLargest is -1. 
Start from index 1, if the second element is larger than first then set secondLargest as Largest and update largest as the second element
Else if currentElement at index 1 is smaller than currentLargest and is greater than the current secondLargest then update the secondLargest element to current array element. 
"""
