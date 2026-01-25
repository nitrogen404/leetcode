class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        result = nums.copy()
        positives = [i for i in nums if i >= 0]
        
        if len(positives) == 0:
            return result

        k %= len(positives)
        rotated = positives[k:] + positives[:k]
        i = 0
        for j in range(len(nums)):
            if nums[j] >= 0:
                result[j] = rotated[i]
                i += 1
        return result