# stockII: http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock-ii/


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit += diff
        return profit