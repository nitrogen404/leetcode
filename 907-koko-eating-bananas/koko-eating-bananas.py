import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            currentSpeed = (low + high) // 2
            totalHours = self.calcSpeed(piles, currentSpeed)
            if totalHours <= h:
                high = currentSpeed - 1
            else:
                low = currentSpeed + 1
        return low

    def calcSpeed(self, piles, speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours