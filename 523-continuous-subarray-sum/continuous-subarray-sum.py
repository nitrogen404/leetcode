class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        hashmap = {0: -1}
        for i, num in enumerate(nums):
            prefix += num
            if k != 0:
                mod = prefix % k
            else:
                mod = prefix
            if mod in hashmap:
                if i - hashmap[mod] >= 2:
                    return True
            else:
                hashmap[mod] = i
        return False
