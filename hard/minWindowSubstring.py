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
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        hasFound = {}
        needToFind = {}
        for char in target:
            if char not in needToFind:
                needToFind[char] = 1
            else:
                needToFind[char] += 1
        start = 0
        count = 0
        result = ""
        minWindow = float("inf")
        for end in xrange(len(source)):
            new_char = source[end]
            if new_char not in needToFind:
                continue

            if new_char not in hasFound:
                hasFound[new_char] = 1
            else:
                hasFound[new_char] += 1
            # compare two hists
            if hasFound[new_char] <= needToFind[new_char]:
                count += 1
            
            if count == len(target):
                while source[start] not in needToFind or hasFound[source[start]] > needToFind[source[start]]:
                    if source[start] in needToFind and hasFound[source[start]] > needToFind[source[start]]:
                        hasFound[source[start]] -= 1
                    start += 1
            
                if len(source[start:end+1]) < minWindow:
                    minWindow = len(source[start:end+1])
                    result = source[start:end+1]
            
        return result

# def minWindow(self, s, t):
#     need, missing = collections.Counter(t), len(t)
#     i = I = J = 0
#     for j, c in enumerate(s, 1):
#         missing -= need[c] > 0
#         need[c] -= 1
#         if not missing:
#             while i < j and need[s[i]] < 0:
#                 need[s[i]] += 1
#                 i += 1
#             if not J or j - i <= J - I:
#                 I, J = i, j
#     return s[I:J]

S = "acbbaca"
T = "aba"
Sol = Solution()
print Sol.minWindow(S, T)
