# permuteII: http://www.lintcode.com/en/problem/permutations-ii/

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        if nums is None or len(nums) == 0:
            return []
        # allows duplicates in input, we should sort it
        nums.sort()
        # since we allow duplicates in the input
        # we use a new list: visited, to keep track of the indices of visited items
        visited = [0] * len(nums)
        self.results = []
        self.DFS([], visited, nums)
        return self.results

    def DFS(self, path, visited, nums):
        # base case
        if len(path) == len(nums):
            # must make new list, list(path). If not, 
            # res (path) points to the obj passed in, which is empty at the beginning
            self.results.append(list(path))
            return

        for i in xrange(len(nums)):
            # continue if the ith number is visited
            # or, it's not visited, it's the same number as the previous, 
            # and the previous was NOT visited
            # AVOID DUPLICATE PERMUTATIONS BY ONLY ALLOWING CONTINUOUS SAME NUMBERS TO BE ADDED TO path
            if visited[i] == 1 or (i != 0 and nums[i] == nums[i-1] and visited[i-1] == 0):
                continue

            visited[i] = 1
            path.append(nums[i])
            self.DFS(path, visited, nums)
            path.pop()
            visited[i] = 0

nums = [1, 1, 2]
Sol = Solution()
print Sol.permuteUnique(nums)



