'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) <= 1:
            return 0
        
        #
        # keep min value to remember min stock value before today;
        # check if sell today, will you get more profit by compare to max_profit;
        # update min price.
        #
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            price = prices[i]
            if price > min_price:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
            elif price < min_price:
                min_price = price
    
        return max_profit
