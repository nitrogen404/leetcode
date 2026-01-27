class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
        result = []
        for num in freqMap:
            if freqMap[num] > len(nums) // 3:
                result.append(num)
        return result
        