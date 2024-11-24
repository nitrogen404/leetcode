"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Come up with O(N) time and O(1) space
"""
# O(N) space O(2N) time
def majorityElement(nums):
    hashmap = {}
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        hashmap[i] = 1
    for i in hashmap:
        if hashmap[i] > len(nums) // 2:
            return i

# O(1) space O(N) time Boyer Mayer's algorithm
def majorityElementOptimal(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if candidate == num:
            count += 1
        else:
            count -= 1
    return candidate