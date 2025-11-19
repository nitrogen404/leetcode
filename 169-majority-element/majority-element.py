class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityElement = None
        count = 0
        for num in nums:
            if count == 0:
                majorityElement = num
                count += 1
            elif num == majorityElement:
                count += 1
            else:
                count -= 1
        return majorityElement