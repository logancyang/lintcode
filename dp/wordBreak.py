# wordBreak: http://www.lintcode.com/en/problem/word-break/

"""
yes/no
State f[i]: bool, can the first i chars be cut
Function: f[i] = any(f[j]), j < i, (j+1)th char to ith char is a word
Init: f[0] = True. For yes/no problems, f[0] = True
Answer: f[len(s)]

Remark:
    Caution, f[i] -> s[:i], so f[i-l] -> s[:i-l], check s[i-l:i] at this time
"""

class Solution:
    # @param s: A string s
    # @param dict: A list of words dict
    def wordBreak(self, s, dict):
        # bug: base case is True
        if s is None or len(s) == 0:
            return True
        # bug: dict cannot be empty to use 'in'
        if len(dict) == 0:
            return False
        # optimization, a word is short
        maxlen = max(len(word) for word in dict)
        # init
        f = [False for i in xrange(len(s)+1)]
        f[0] = True
        # function. here i represents the actual ith char
        # i loop from 1 to n+1, s[:i] from 1st char to nth since s[:n+1] = s[:n]
        for i in xrange(1, len(s)+1):
            # l loops backwards for word length optimization
            # caution: + 1, or the l loop range is wrong, it won't reach bound_l if not + 1
            bound_l = min(maxlen, i) + 1
            # print "loop i", i
            for l in xrange(1, bound_l):
                # the first i-l chars
                # print "f[", i-l, "]", "s[", i-l, ":", i, "]", s[i-l:i]
                if not f[i-l]:
                    continue
                # i-l 
                if s[i-l:i] in dict:
                    f[i] = True
                    # print "f[", i, "] set to True"
                    break
        # answer
        return f[-1]

# s = "lintcode"
# dic = ["lint", "code"]
S = "aaab"
d = ["b", "aa"]
Sol = Solution()
print Sol.wordBreak(S, d)