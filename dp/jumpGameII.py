# jumpGameII: http://www.lintcode.com/en/problem/jump-game-ii/
import random


class Solution:
    # @param A, a list of integers
    # @return an integer
    # DP solution, O(n^2)
    def jumpMy(self, A):
        # init, cannot reach -> inf
        inf = float("inf")
        f = [inf for item in A]
        f[0] = 0
        # function: if f[j] and j + A[j] >= i, f[i] = f[j] + 1
        for i in xrange(1, len(A)):
            minstep = inf
            for j in xrange(i):
                if f[j] != inf and j + A[j] >= i and f[j] + 1 < minstep:
                    minstep = f[j] + 1
            f[i] = minstep
        # answer
        return f

    def jumpAnswer(self, A):
        # init, cannot reach -> inf
        inf = float("inf")
        f = [inf for item in A]
        f[0] = 0
        # function: if f[j] and j + A[j] >= i, f[i] = f[j] + 1
        for i in xrange(1, len(A)):
            for j in xrange(i):
                if f[j] != inf and j + A[j] >= i:
                    f[i] = f[j] + 1
                    # since f is increasing, we don't need to continue, 
                    # f[i] already got its min
                    break
        # answer
        return f

    # 2-pointers: O(n)
    def jump2pointers(self, A):
        if A is None or len(A) == 0:
            return 0
        # bug
        # input: [0]
        # expect: 0
        if len(A) == 1:
            return 0
        n = len(A)
        start = 0
        end = 0
        steps = 0
        while end < n - 1:
            maxim = 0
            steps += 1
            for i in xrange(start, end+1):
                maxim = max(maxim, i + A[i])
                if maxim >= n - 1:
                    return steps
            start = end + 1
            end = maxim
            if start > end:
                break
        return float("inf")



S = [random.randint(0, 5) for j in xrange(10)]
print S
Sol = Solution()
print Sol.jumpMy(S)
print Sol.jumpAnswer(S)
