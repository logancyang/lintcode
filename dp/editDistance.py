# editDistance: http://www.lintcode.com/en/problem/edit-distance/

"""
min/max
State f[i][j]: the min steps from the first i chars in word1 to the first j chars in word2
Function:
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
Init: f[0][j] = j, f[i][0] = i
Answer: f[-1][-1]
"""

class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        # init
        f = [[j if i == 0 else i if j == 0 else 0 for j in xrange(n+1)] for i in xrange(m+1)]
        # function
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
        # answer
        return f[-1][-1]

A = ""
B = ""
Sol = Solution()
print Sol.minDistance(A, B)


