# stockI: http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock/
# 1 transaction, find max_profit

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0

        prev_min = float("inf"); max_profit = 0
        accumulator = 0
        for i in xrange(len(prices)):
            # for prices[i] as selling point, max_diff = prices[i] - prev_min --> local max_profit
            # compare with global max_profit
            max_profit = max(max_profit, prices[i] - prev_min)
            # this prev_min is for the next i
            prev_min = min(prev_min, prices[i])
        return max_profit

A = [1, 2]
Sol = Solution()
print Sol.maxProfit(A)