# LCSubstring: http://www.lintcode.com/en/problem/longest-common-substring/

"""
min/max
State f[i][j]: the first i chars in A against the first j chars in B, the LCSubstring
Function:
    # i, j from 1 -> len+1 exclusive, meaning A[i-1] is the ith char
    if A[i-1] == B[j-1]:
        f[i][j] = f[i-1][j-1] + 1
    else:
        f[i][j] = 0
Init: f[i][0] = 0, f[0][j] = 0
Answer: max(f[][])
"""

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        if A is None or B is None:
            return 0
        m = len(A)
        n = len(B)
        if m == 0 or n == 0:
            return 0
        # init
        f = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
        # function
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = 0
        # answer
        return max(max(row) for row in f)

A = "ABCD"
B = "CBCE"
Sol = Solution()
print Sol.longestCommonSubstring(A, B)