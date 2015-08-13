# uniquePath II: http://www.lintcode.com/en/problem/unique-paths-ii/
import random
class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid is None or len(obstacleGrid) == 0 \
        or obstacleGrid[0][0] != 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # init:
        f = [[0 for j in xrange(n)] for i in xrange(m)]
        f[0][0] = 1
        first_row = obstacleGrid[0]
        first_col = [obstacleGrid[i][0] for i in xrange(m)]
        # all grids in 1st row and col have 1 if no obstacle
        # all 0 after hitting obstacle
        for j in xrange(1, n):
            if obstacleGrid[0][j] == 0:
                f[0][j] = 1
            else:
                break
        for i in xrange(1, m):
            if obstacleGrid[i][0] == 0:
                f[i][0] = 1
            else:
                break
        # function
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] != 0:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        # answer
        return f[-1][-1]

# random.seed(1023)
S = [[0 for j in xrange(4)] for i in xrange(4)]
S[2][3] = 1
print S
Sol = Solution()
print Sol.uniquePathsWithObstacles(S)