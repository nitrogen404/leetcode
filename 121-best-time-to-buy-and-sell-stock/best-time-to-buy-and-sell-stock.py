class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp, sp, profit = 0, 0, 0
        while sp < len(prices):
            if prices[sp] > prices[cp]:
                profit = max(profit, prices[sp] - prices[cp])
            else:
                cp = sp
            sp += 1
        return profit
            