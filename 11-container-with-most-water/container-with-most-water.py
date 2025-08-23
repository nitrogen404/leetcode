class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea, left, right = 0, 0, len(height) - 1
        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        return maxArea