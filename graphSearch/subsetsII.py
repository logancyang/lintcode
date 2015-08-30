# subsetsII: http://www.lintcode.com/en/problem/subsets-ii/

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        if S is None or len(S) == 0:
            return []
        S.sort()
        self.results = []
        self.DFS([], 0, S)

        return self.results

    def DFS(self, path, ind, S):
        # base case, add each path of each recursion (sorted as required)
        # must make new list, list(path). If not, 
        # res (path) points to the obj passed in, which is empty at the beginning
        res = list(path)
        self.results.append(res)
        # i is the first item's index in a path
        for i in xrange(ind, len(S)):
            # THE ONLY DIFFERENCE WITH SUBSETS I: 
            # continue if current number == previous number
            if i != ind and S[i] == S[i-1]:
                continue
            path.append(S[i])
            self.DFS(path, i+1, S)
            path.pop()

S = [1, 2, 2]
Sol = Solution()
print Sol.subsetsWithDup(S)