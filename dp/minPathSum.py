# minPathSum: http://www.lintcode.com/en/problem/minimum-path-sum/
import random

class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if grid is None or len(grid) == 0:
            return 0
        # init
        f = [[float("inf") for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
        first_row = grid[0]
        first_col = [grid[i][0] for i in xrange(len(grid))]
        # init 1st col, i inclusive
        for i in xrange(len(grid)):
            f[i][0] = sum(first_col[:i+1])
        # init 1st row, j inclusive
        for j in xrange(len(grid[0])):
            f[0][j] = sum(first_row[:j+1])
        # function
        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])):
                f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
        # answer
        return f[-1][-1]

random.seed(1023)
S = [[random.randint(0, 10) for j in xrange(4)] for i in xrange(4)]
print S
Sol = Solution()
print Sol.minPathSum(S)