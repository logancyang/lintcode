# minWindowSubstring: http://www.lintcode.com/en/problem/minimum-window-substring/#

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"

Thoughts:

hasFound['a'] = #
needToFind['a'] = #

"""


class Solution:
    # @return a string
    def minWindow(self, S, T):
        if S is None or T is None:
            return ""
        if len(S) == 0 or len(T) == 0:
            return ""
        hasFound = {}
        needToFind = {}
        for char in T:
            if char not in needToFind:
                needToFind[char] = 1
            else:
                needToFind[char] += 1
        start = 0
        count = 0
        result = ""
        minlen = float("inf")
        for end in xrange(len(S)):
            # make hasFound hist for current window until hist has all keys and values of needToFind
            char = S[end]
            if char not in T:
                continue
            # update hasFound hist
            if char not in hasFound:
                hasFound[char] = 1
            else:
                hasFound[char] += 1
            # count # of T's char in window
            # keep count unchanged if has[] exceed the need[]
            # and when has[] > need[], roll start forward
            if hasFound[char] <= needToFind[char]:
                count += 1
            # if window found
            if count == len(T):
                # for or: needToFind[key_not_exists] is fine
                while S[start] not in T or hasFound[S[start]] > needToFind[S[start]]:
                    # for and: needToFind[key_not_exists] is NOT fine
                    if S[start] in T and hasFound[S[start]] > needToFind[S[start]]:
                        hasFound[S[start]] -= 1
                    start += 1

                if len(S[start:end+1]) < minlen:
                    minlen = len(S[start:end+1])
                    result = S[start:end+1]

        return result

# S = "ADOBECODEBANC"
# T = "ABC"
S = "acbbaca"
T = "aba"
Sol = Solution()
print Sol.minWindow(S, T)
