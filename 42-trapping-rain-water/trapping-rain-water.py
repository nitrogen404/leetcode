class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        total, l_max, r_max = 0, 0, 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] > l_max:
                    l_max = height[l]
                else:
                    total += l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    total += r_max - height[r]
                r -= 1

        return total