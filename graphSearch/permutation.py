# permutation: http://www.lintcode.com/en/problem/permutations/

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if nums is None or len(nums) == 0:
            return []

        self.results = []
        self.DFS([], nums)
        return self.results

    def DFS(self, path, nums):
        # base case
        if len(path) == len(nums):
            # must make new list, list(path). If not, 
            # it points to the obj passed in, which is empty at the beginning
            self.results.append(list(path))
            return

        for i in xrange(len(nums)):
            # check if the ith number is already in path
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.DFS(path, nums)
            path.pop()

nums = [1, 2, 3]
Sol = Solution()
print Sol.permute(nums)