# Subsets: http://www.lintcode.com/en/problem/subsets/

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        if S is None or len(S) == 0:
            return []

        self.results = []
        self.DFS([], 0, S)
        return self.results

    def DFS(self, path, ind, S):
        # no base case, add all paths (sorted as required)
        res = list(path)
        res.sort()
        self.results.append(res)

        for i in xrange(ind, len(S)):
            path.append(S[i])
            self.DFS(path, i+1, S)
            path.pop()

S = [1, 2, 3]
Sol = Solution()
print Sol.subsets(S)