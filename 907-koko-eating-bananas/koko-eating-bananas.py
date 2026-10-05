class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            total_time = self.calculate_hours(mid, piles)
            if total_time <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def calculate_hours(self, speed, piles):
        total_time = 0
        for bananas in piles:
            total_time += math.ceil(bananas / speed)
        return total_time

