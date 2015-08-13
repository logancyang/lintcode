# uniquePath: http://www.lintcode.com/en/problem/unique-paths/

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # init: 1 path at least, the 1st row and col
        f = [[1 for j in xrange(n)] for i in xrange(m)]
        # function
        for i in xrange(1, m):
            for j in xrange(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]
        # answer
        return f[-1][-1]