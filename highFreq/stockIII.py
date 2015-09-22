# stockIII: http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock-iii/

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0
        # store the max_profit for the left and right parts
        left = [0] * len(prices)
        right = [0] * len(prices)
        # left, scan left to right
        # local = prices[i] - curr_min
        curr_min = prices[0]
        for i in xrange(1, len(prices)):
            curr_min = min(curr_min, prices[i])
            left[i] = max(left[i-1], prices[i] - curr_min)
            
        # right, scan right to left
        # different from left. local = curr_max - prices[i]
        curr_max = prices[-1]
        for i in xrange(len(prices)-2, -1, -1):
            curr_max = max(curr_max, prices[i])
            right[i] = max(right[i+1], curr_max - prices[i])

        max_profit = max([left[i] + right[i] for i in xrange(len(prices))])
        return left, right
        # return max_profit

A = [4,4,6,1,1,4,2,5]
Sol = Solution()
print Sol.maxProfit(A)
