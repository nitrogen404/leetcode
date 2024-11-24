"""
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.
"""

def leaders(arr):
    allLeaders = [arr[-1]]
    maxElement = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= maxElement:
            maxElement = arr[i]
            allLeaders.append(maxElement)
    return allLeaders

print(leaders([10, 4, 2, 4, 1]))
