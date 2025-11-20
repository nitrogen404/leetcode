class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        l = 0
        windowSum = 0
        for r in range(len(arr)):
            windowSum += arr[r]
            if (r - l + 1) == k:
                if windowSum >= threshold * k:
                    result += 1
                windowSum -= arr[l]
                l += 1

        return result