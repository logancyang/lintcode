# distinctSubseq: http://www.lintcode.com/en/problem/distinct-subsequences/

"""
count # solutions: # subsequences of S == T
State f[i][j]: the # solutions for the first i of S and the first j of T
Function: 
                if S[i-1] == T[j-1]:
                    f[i][j] = f[i-1][j] + f[i-1][j-1]
                else:
                    f[i][j] = f[i-1][j]
Init: f[i][0] = 1, f[0][j] = 0, j>0
Answer: f[-1][-1]
"""

class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        m = len(S)
        n = len(T)
        # init
        f = [[1 if j == 0 else 0 for j in xrange(n+1)] for i in xrange(m+1)]
        # function
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if S[i-1] == T[j-1]:
                    f[i][j] = f[i-1][j] + f[i-1][j-1]
                else:
                    f[i][j] = f[i-1][j]
        # answer
        return f[-1][-1]

S = "aba"
T = "a"
Sol = Solution()
print Sol.numDistinct(S, T)