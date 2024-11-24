"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


"""

def maxProfit(prices):
    profit = 0
    costPrice, sellingPrice = 0, 1
    while sellingPrice < len(prices):
        if prices[costPrice] < prices[sellingPrice]:
            profit = max(profit, prices[sellingPrice] - prices[costPrice])
        else:
            costPrice = sellingPrice
        sellingPrice += 1
    return profit

