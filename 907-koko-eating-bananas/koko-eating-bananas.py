class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            current_rate = (low + high) // 2
            current_time = 0
            for bananas in piles:
                current_time += math.ceil(bananas / current_rate)
            
            if current_time <= h:
                high = current_rate - 1
            else:
                low = current_rate + 1

        return low
                
