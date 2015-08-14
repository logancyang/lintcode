# palinPartitionII: http://www.lintcode.com/en/problem/palindrome-partitioning-ii/

"""
# Solution
State f[i]: min # cuts for the first i chars, s[:i] (i exclusive)
Function: f[i] = min(f[j]+1), j < i and s[j:i] isPalindrome. j -> 0:i
Init: f[i] = i-1, f[0] = -1
Answer: f[-1]
"""


class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if s is None or len(s) == 0:
            return 0
        n = len(s)
        # len(f) = len(s) + 1, because s[] -> f = -1, s[0] -> f = 0
        f = [i-1 for i in xrange(n+1)]
        # tups_cut = []
        # i from 1 -> n+1, since len(f) = n+1
        for i in xrange(1, n+1):
            # tups_cut.append(i)
            for j in xrange(i):
                # tup = s[j:i]
                # tups_cut.append(tup)
                if self.isPalindrome(s[j:i]):
                    f[i] = min(f[i], f[j]+1)
                    # tups_cut.append("f["+str(i)+"] = "+ str(f[i]))

        return f

    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

a = "abbv"
Sol = Solution()
# print Sol.isPalindrome(a)
print Sol.minCut(a)