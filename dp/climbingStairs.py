# climbingStairs: http://www.lintcode.com/en/problem/climbing-stairs/

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # corner cases, n = 0, 1, 2
        if n <= 2:
            return n
        f = [0 for i in xrange(n)]
        # init
        f[0] = 1
        f[1] = 2
        # function
        for i in xrange(2, n):
            f[i] = f[i-1] + f[i-2]
        # answer
        return f[-1]