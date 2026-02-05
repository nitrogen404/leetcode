class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp, sp, maxProfit = 0, 0, 0
        while sp < len(prices):
            if prices[cp] < prices[sp]:
                profit = prices[sp] - prices[cp]
                maxProfit = max(maxProfit, profit)
            else:
                cp = sp
            sp += 1
        return maxProfit