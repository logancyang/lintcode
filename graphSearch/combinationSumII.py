# combinationSumII: http://www.lintcode.com/en/problem/combination-sum-ii/

class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
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
            # recurse down from index i
            path.append(self.candidates[i])
            # THE ONLY DIFFERENCE WITH COMBINATION SUM I: i+1
            self.DFS(target - self.candidates[i], path, i+1)
            path.pop()

            prev = self.candidates[i]

candidates = [1,6,7,2,1]
target = 8
Sol = Solution()
print Sol.combinationSum2(candidates, target)

