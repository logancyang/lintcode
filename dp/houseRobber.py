# houseRobber: http://www.lintcode.com/en/problem/house-robber/

class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        n = len(A)
        res = [0] * n
        ans = 0
        if n == 0:
            return 0
        if n >= 1:
            res[0] = A[0]
        if n >= 2:
            res[1] = max(A[0], A[1])
        if n >= 3:
            res[2] = max(A[0]+A[2], A[1])
        if n > 3:
            # for i-4, i-3, i-2, i-1, i
            # have i, i-1 must be x, i-2 can be ok, i-3 x, i-4 ok
            # have i, i-1 must be x, i-2 can be x, i-3 ok, i-4 x 
            for i in xrange(3, n):
                res[i] = max(res[i-3], res[i-2]) + A[i]
        return max(res)
