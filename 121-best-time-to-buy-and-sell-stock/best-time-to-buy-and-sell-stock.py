class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cp, sp, maxProfit = 0, 0, 0
        while sp < len(prices):
            if prices[cp] < prices[sp]:
                maxProfit = max(maxProfit, prices[sp] - prices[cp])
            else:
                cp = sp
            sp += 1
        return maxProfit
        