""""
Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k
"""

"""
WORKS ONLY FOR ARRAY WITH POSITIVE NUMBERS
"""

# O(n2) Time O(1) Space
def longestSubArrayBrute(array, k):
    # brute force
    maxLength = 0
    for i in range(len(array)):
        for j in range(len(array)):
            tempArray = array[i: j + 1]
            if sum(tempArray) == k:
                maxLength = max(maxLength, len(tempArray))
    return maxLength


# O(N) Time O(N) Space 
"""WORKS FOR NEGTIVE  NUMBERS AS WELL """
def longestSubArrayOptimal(array, k):
    map = {} # {SumSoFar: index until that sum} {10: 0, 15: 1, 17: 2, 24: 3, 25: 4, 34: 5}
    Sum = 0
    maxLength = 0
    for i in range(len(array)):
        Sum += array[i]
        
        if Sum == k:
            maxLength = max(maxLength, i + 1)
        
        if Sum not in map:
            map[Sum] = i
        
        rem_ = Sum - k
        if rem_ in map:
            length = i - map[rem_]
            maxLength = max(maxLength, length)
        
    return maxLength


# O(N) Time O(1) Space
"""WORKS ONLY FOR POSTIIVE NUMBERS"""
def longestSubArrayBest(array, k):
    left = 0
    right = 0
    maxLen = 0
    Sum = array[0]
    while right < len(array):
        while left <= right and Sum > k:
            Sum -= array[left]
            left += 1
        
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)
        
        right += 1
        if right < len(array): 
            Sum += array[right]
    return maxLen

print(longestSubArrayBest([10, 5, 2, 7, 1, 9], 15))

