class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        hashmap = {}
        for i in range(len(nums2) - 1, -1, -1):
            while stk and stk[-1] < nums2[i]:
                stk.pop()
            if stk:
                hashmap[nums2[i]] = stk[-1]
            else:
                hashmap[nums2[i]] = -1
            stk.append(nums2[i])
        return [hashmap[i] for i in nums1]
        