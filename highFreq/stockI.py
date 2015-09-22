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

        curr_min = prices[0]
        max_profit = 0

        for i in xrange(len(prices)):
            # up to ith item, the min item
            curr_min = min(curr_min, prices[i])
            # global_max = max(global_max, local_max for ith)
            max_profit = max(max_profit, prices[i] - curr_min)
        return max_profit

A = [1, 2]
Sol = Solution()
print Sol.maxProfit(A)