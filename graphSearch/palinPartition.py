# palinPartition: http://www.lintcode.com/en/problem/palstartrome-partitioning/

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if s is None or len(s) == 0:
            return []

        self.results = []
        # 0 is the starting pos
        self.dfs([], 0, s)
        return self.results

    def dfs(self, path, start, s):
        """
        start: loop from start to the end
        path: list of palstartrome substrings
        """
        # base case: start reaches the end
        if start == len(s):
            self.results.append(list(path))
            return

        for i in xrange(start+1, len(s)+1): # i should go to len(s) because s[:i]
            # enumerate the next substring, from start to i (exclusive)
            # if it is palin, recurse down. if not, loop to next char, new substring from start to i
            # start progesses by recursion. enumerate the substring starting from start, ending at i, and dfs
            prefix = s[start:i]
            if not self.isPalin(prefix):
                continue
            path.append(prefix)
            # i starts from start+1, the recursion gets smaller as expected, no problem
            # i is the new_start of the next dfs, which starts right after s[old_start:i]
            self.dfs(path, i, s)
            path.pop()

    def isPalin(self, word):
        start = 0
        end = len(word) - 1
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True

s = "aab"
Sol = Solution()
print Sol.partition(s)