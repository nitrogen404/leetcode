

def singleNumber(nums):
    map = {}
    for i in nums:
        if i in map:
            map[i] += 1
        else: map[i] = 1    

def singleNumberXOR(nums):
    res = 0
    for i in nums:
        res ^= i
    return res

singleNumber([4, 1, 2, 1, 2])
