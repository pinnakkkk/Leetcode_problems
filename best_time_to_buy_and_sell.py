'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min = prices[0]

        for i in range(1, len(prices)):
            if curr_min > prices[i]:
                curr_min = prices[i]
            elif (prices[i] - curr_min) > max_profit:
                max_profit = prices[i] - curr_min
        
        return max_profit
