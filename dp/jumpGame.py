# jumpGame: http://www.lintcode.com/en/problem/jump-game/
# Greedy is best O(n), DP is O(n^2).

class Solution:
    # @param A, a list of integers
    # @return a boolean
    # DP solution
    def canJump(self, A):
        if A is None or len(A) == 0:
            return False
        # init
        f = [False] * len(A)
        f[0] = True
        # function
        for i in xrange(1, len(A)):
            for j in xrange(i):
                reachable_from_j = (j + A[j] >= i)
                if f[j] and reachable_from_j:
                    f[i] = True
                    # break the j loop
                    # irrelevant: if want to break from outer loop, just use a flag
                    # once we break the inner, set flag to True, check in outer loop and break
                    break
        # answer
        return f[-1]

    # Greedy solution, O(n)
    def canJumpGreedy(self, A):
        if A is None or len(A) == 0:
            return False
        n = len(A)
        rightmost = 0
        # i must not exceed current rightmost, actually, because it's not reachable
        for i in xrange(n):
            # prev rightmost, and current rightmost
            rightmost = max(rightmost, i + A[i])
            # check if already succeeded in reaching the end
            if rightmost >= n - 1:
                return True
            # i must not exceed rightmost
            # i reached the rightmost, cannot go further
            if i == rightmost:
                return False
        return True