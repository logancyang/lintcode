# Longest Common Subsequence: http://www.lintcode.com/en/problem/longest-common-subsequence/

"""
min/max
State f[i][j]: first i chars in sequence a against first j chars in sequence b, the LCSeq length
Function: 
    if a[i-1] == b[j-1]:
        f[i][j] = f[i-1][j-1] + 1
    else:
        f[i][j] = max(f[i-1][j], f[i][j-1])
Init: fdim = (len(a)+1, len(b)+1), f[i][0] = 0, f[0][j] = 0
Answer: f[-1][-1], or f[len(a)][len(b)]
"""


class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
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
                # for dp problems where f[0] or f[0][0] refers to no char,
                # loop i from 1 -> n+1, then string[i-1] is the ith char
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1])
        # answer
        return f[-1][-1]

A = "ABCD"
B = "EACB"
Sol = Solution()
print Sol.longestCommonSubsequence(A, B)
