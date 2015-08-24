# interleavingString: http://www.lintcode.com/en/problem/interleaving-string/

"""
yes/no
State f[i][j]: can the first i chars in s1, and the first j chars in s2,
               interleave to produce the first i+j chars in s3
Function: 
        f[i][j] = (f[i-1][j] and s1[i-1] == s3[i+j-1]) or
                  (f[i][j-1] and s2[j-1] == s3[i+j-1])
        Comment: can the first i-1 chars of s1 and first j chars in s2 get
                 first i-1+j chars in s3, and in the case that, 
                 the ith char in s1 matches the (i+j)th char in s3.
                 Or,
                 ...
Init: f[i][0] = (s1[:i] == s3[:i]), f[0][j] = (s2[:j] == s3[:j])
Answer: f[-1][-1]

Remarks:
len(s3) = len(s1) + len(s2)
keep relative order in each string in the result string
"""

class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m+n != l:
            return False
        # init
        f = [[False] * (n+1) for i in xrange(m+1)]
        f[0][0] = True
        for i in xrange(1, m+1):
            f[i][0] = (s1[:i] == s3[:i])
        for j in xrange(1, n+1):
            f[0][j] = (s2[:j] == s3[:j])
        # function
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                s1last = f[i-1][j] and (s1[i-1] == s3[i+j-1])
                s2last = f[i][j-1] and (s2[j-1] == s3[i+j-1])
                f[i][j] = s1last or s2last
        # answer
        return f[-1][-1]

