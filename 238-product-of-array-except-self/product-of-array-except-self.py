class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct, suffixProduct = 1, 1
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        for i in range(len(nums)):
            j = -i - 1
            prefix[i] = prefixProduct
            suffix[j] = suffixProduct
            prefixProduct *= nums[i]
            suffixProduct *= nums[j]
        return [prefix[i] * suffix[i] for i in range(len(nums))]
