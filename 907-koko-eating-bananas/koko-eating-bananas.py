class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            current_time = 0
            for bananas in piles:
                current_time += math.ceil(bananas / mid)
            if current_time <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low