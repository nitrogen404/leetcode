class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 0:
            return 0
            
        left_max = [0] * len(height)
        left_max[0] = height[0]
        
        right_max = [0] * len(height)
        right_max[-1] = height[-1]

        for i in range(1, len(left_max)):
            left_max[i] = max(left_max[i - 1], height[i])
        
        for i in range(len(right_max) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        total = 0
        for i in range(len(height)):
            max_height = min(left_max[i], right_max[i])
            if max_height > height[i]:
                total += max_height - height[i]

        return total