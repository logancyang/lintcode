# combinationSum: http://www.lintcode.com/en/problem/combination-sum/

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        if candidates is None or len(candidates) == 0:
            return []

        self.results = []
        self.candidates = candidates
        candidates.sort()
        # target gets smaller when recursing down
        self.DFS(target, [], 0)
        return self.results

    def DFS(self, target, path, curr_ind):
        # base case
        if target == 0:
            self.results.append(list(path))
            return

        prev = -1
        # recurse down
        for i in xrange(curr_ind, len(self.candidates)):
            # do not recurse when the sum is going to exceed target
            if self.candidates[i] > target:
                break
            # encounter the same number again, continue to next index
            if prev == self.candidates[i]:
                continue
            # recurse down from index i, not i+1 since we can use the same number multiple times
            path.append(self.candidates[i])
            self.DFS(target - self.candidates[i], path, i)
            path.pop()

            prev = self.candidates[i]

candidates = [2, 3, 6, 7]
target = 7
Sol = Solution()
print Sol.combinationSum(candidates, target)
