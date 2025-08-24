class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total, lMax, rMax = 0, 0, 0
        while l < r:
            if height[l] <= height[r]:
                if height[l] < lMax:
                    total += lMax - height[l]
                else:
                    lMax = height[l]
                l += 1
            else:
                if height[r] < rMax:
                    total += rMax - height[r]
                else:
                    rMax = height[r]
                r -= 1
        return total
                