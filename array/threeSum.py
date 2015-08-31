# threeSum: http://www.lintcode.com/en/problem/3-sum/

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    # slow: DFS
    def threeSumSearch(self, numbers):
        if numbers is None or len(numbers) == 0:
            return []
        numbers.sort()
        self.results = []
        self.dfs([], 0, numbers)
        return self.results

    def dfs(self, path, ind, numbers):
        # base case
        if len(path) == 3 and sum(path) == 0:
            self.results.append(list(path))
            return

        for i in xrange(ind, len(numbers)):
            if i != ind and numbers[i] == numbers[i-1]:
                continue
            path.append(numbers[i])
            self.dfs(path, i+1, numbers)
            path.pop()

    # fast: 2-pointers meet
    

numbers = [-1, 0, 1, 2, -1, -4]
Sol = Solution()
print Sol.threeSum(numbers)
