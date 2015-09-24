# flip bits: http://www.lintcode.com/en/problem/flip-bits/
# Hamming distance: https://en.wikipedia.org/wiki/Hamming_weight


class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    # for positives
    def bitSwapRequired(self, a, b):
        n = a ^ b
        count = 0
        while n > 0:
            count += 1
            n = n & (n - 1)
        return count

a = 31
b = 14
Sol = Solution()
print Sol.bitSwapRequired(a, b)
