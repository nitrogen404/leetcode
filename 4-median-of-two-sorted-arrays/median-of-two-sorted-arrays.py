class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        prev, current = 0, 0
        i, j = 0, 0
        count = 0
        for count in range((m + n) // 2 + 1):
            prev = current
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                current = nums1[i]
                i += 1
            else:
                current = nums2[j] 
                j += 1
    
        if (m + n) % 2 == 1:
            return current
        else:
            return (prev + current) / 2