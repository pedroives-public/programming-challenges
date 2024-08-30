"""
You are given an array prices where prices[i] is the price of a given stock on 
the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like, but you need to pay the transaction fee for each transaction.

Note:
You may not engage in multiple transactions simultaneously (i.e., you must sell 
the stock before you buy again). The transaction fee is only charged once for 
each stock purchase and sale.

Example 1:

    Input: prices = [1,3,2,8,4,9], fee = 2
    Output: 8
    Explanation: The maximum profit can be achieved by:
    - Buying at prices[0] = 1
    - Selling at prices[3] = 8
    - Buying at prices[4] = 4
    - Selling at prices[5] = 9
    The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:

    Input: prices = [1,3,7,5,10,3], fee = 3
    Output: 6


Problem Source: LeetCode

Solution -> O(n)
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp_not_bought = [0] * (n + 1)
        dp_bought = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp_not_bought[i] = max(dp_not_bought[i+1], dp_bought[i+1] + prices[i] - fee)
            dp_bought[i] = max(dp_bought[i+1], dp_not_bought[i+1] - prices[i])
        
        return dp_bought[0]