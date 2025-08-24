class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        rightMax[len(height) - 1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        total = 0
        for i in range(len(height)):
            waterLevel = min(leftMax[i], rightMax[i])
            if waterLevel > height[i]:
                total += waterLevel - height[i]
        return total 
            
            
        