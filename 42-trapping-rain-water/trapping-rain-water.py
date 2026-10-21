class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        total = 0 
        while l < r:
            if height[l] <= height[r]:
                if lmax < height[l]:
                    lmax = height[l]
                else:
                    total += lmax - height[l]
                l += 1
            else:
                if rmax < height[r]:
                    rmax = height[r]
                else:
                    total += rmax - height[r]
                r -= 1
        return total