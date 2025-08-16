class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd, suffixProd = 1, 1
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        for i in range(n):
            j = -i - 1
            prefix[i] = prefixProd
            suffix[j] = suffixProd
            prefixProd *= nums[i]
            suffixProd *= nums[j]
        
        return [prefix[i] * suffix[i] for i in range(n)]