class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp, sp, maxProfit = 0, 0, 0
        while sp < len(prices):
            if prices[sp] > prices[cp]:
                profit = prices[sp] - prices[cp]
                maxProfit += profit
                cp = sp
            else:
                cp = sp
            sp += 1
        return maxProfit