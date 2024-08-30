"""
You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like (i.e., buy one and sell one share of the stock multiple times) with 
the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must 
sell the stock before you buy again).

Example 1:

    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

    Input: prices = [1]
    Output: 0


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dp(idx, canBuy):
            if idx >= n:
                return 0
            
            if not canBuy:
                sell = dp(idx + 2, not canBuy) + prices[idx]
                ignore = dp(idx + 1, canBuy)
                return max(sell, ignore)
            else:
                buy = dp(idx + 1, not canBuy) - prices[idx]
                ignore = dp(idx + 1, canBuy)
                return max(buy, ignore)
        
        return dp(0, 1)