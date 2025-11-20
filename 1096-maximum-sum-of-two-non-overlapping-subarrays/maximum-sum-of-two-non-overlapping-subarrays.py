class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def maxSum(fl, sl):
            prefix = [0] * (len(nums) + 1)
            for i in range(len(nums)):
                prefix[i + 1] = prefix[i] + nums[i]

            maxSumFirst = 0
            result = 0
            for i in range(fl + sl, len(nums) + 1):
                first = prefix[i - sl] - prefix[i - sl - fl]
                second = prefix[i] - prefix[i - sl]
                maxSumFirst = max(maxSumFirst, first)
                result = max(result, maxSumFirst + second)
            return result
        
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))




            