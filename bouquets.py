# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/


# optimal
def usingBinarySearch(bloomDay, m, k):
    low, high = min(bloomDay), max(bloomDay)
    while low <= high:
        mid = (low + high) // 2
        numberOfBouquets = possible(bloomDay, mid, m, k)
        if numberOfBouquets:
            high = mid - 1
        else:
                low = mid + 1
    return low

# brute force. 
def minDays(bloomDay, m, k):
        if m * k > len(bloomDay): return - 1

        for i in range(min(bloomDay), max(bloomDay) + 1):
            if possible(bloomDay, i, m, k):
                return i
        return -1


def possible(array, day, m, k):
    counter = 0
    possibleBouquets = 0
    for i in range(len(array)):
        if array[i] <= day:
            counter += 1
        else:
            possibleBouquets += counter // k
            counter = 0
    possibleBouquets += counter // k
    return possibleBouquets >= m
 
print(minDays([1,10,3,10,2], 3, 1))


"""
Minimum number of days required to bloom atleast one flower is min(bloomDay) and for all the flowers to bloom, we need max(bloomDay) days. 

In brute force, we iterate from min(bloomDay) to max(bloomDay) and for every single day, check how many flowers bloom and if we can make m or greater bouquets with k consecutive flowers. 

Apply binary search on range of days from min(bloomDay) to max(bloomDay). If we get numberOfBouquets, then we need to find the minimum days so high = mid - 1, else low = mid + 1

"""