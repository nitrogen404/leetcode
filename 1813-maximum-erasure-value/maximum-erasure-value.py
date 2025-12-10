class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        score = 0
        currentScore = 0
        seen = set()
        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                currentScore -= nums[l]
                l += 1
            seen.add(nums[r])
            currentScore += nums[r]
            score = max(score, currentScore)
        return score