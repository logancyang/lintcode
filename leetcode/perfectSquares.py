# perfectSquares: Given a positive integer n, find the least number of perfect square numbers 
# (for example, 1, 4, 9, 16, ...) which sum to n.
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, 
# return 2 because 13 = 4 + 9.

import math

class Solution(object):
    # TLE
    def numSquaresDFS(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxnum = int(math.sqrt(n))
        candidates = [x**2 for x in xrange(1, maxnum+1)]
        candidates = candidates[::-1]
        path = []
        self.result = float("inf")
        self.dfs(candidates, 0, path, n)
        return self.result

    def dfs(self, candidates, ind, path, target):
        # base case
        if sum(path) == target and len(path) < self.result:
            self.result = len(path)
            return
        if len(path) >= self.result:
            return
        # recursion
        for i in xrange(ind, len(candidates)):
            if sum(path) > target:
                return
            path.append(candidates[i])
            self.dfs(candidates, ind, path, target)
            path.pop()

    # Working solution: static DP
    numSquaresDP = [0]
    def numSquares(self, n):
        if len(self.numSquaresDP) <= n:
            perfectSqr = [v**2 for v in xrange(1, int(math.sqrt(n)) + 1)]
            for i in xrange(len(self.numSquaresDP), n + 1):
                self.numSquaresDP.append( min(1 + self.numSquaresDP[i - sqr] 
                    for sqr in perfectSqr if sqr <= i))
        return self.numSquaresDP[n] 


Sol = Solution()
print Sol.numSquares(13)
