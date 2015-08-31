# longestCommonPrefix: http://www.lintcode.com/en/problem/longest-common-prefix/

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    # method 1: slow, compare strings
    def longestCommonPrefixI(self, strs):
        if strs is None or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        done = False
        prefix_len = 1
        prev = ""
        while not done:
            prefix = strs[0][:prefix_len]
            for i in xrange(1, len(strs)):
                if strs[i][:prefix_len] != prefix:
                    return prev
            prefix_len += 1
            prev = prefix
        return

    # fast, compare chars!
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        # set prefix as the 1st string
        prefix = strs[0]
        # loop over all strings, 
        for i in xrange(1, len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(prefix) and strs[i][j] == prefix[j]:
                j += 1
            if j == 0:
                return ""
            prefix = prefix[:j]
        return prefix


strs = ["aac","acab","aa","abba","aa"]
Sol = Solution()
print Sol.longestCommonPrefix(strs)
