class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cp, sp, profit = 0, 0, 0
        while sp < len(prices):
            if prices[cp] < prices[sp]:
                profit += prices[sp] - prices[cp]
                cp += 1
            else:
                cp = sp
            sp += 1
        return profit