# threeSum (two-pointers meet): http://www.lintcode.com/en/problem/3-sum/

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    # slow: DFS
    def threeSumSearch(self, numbers):
        if numbers is None or len(numbers) < 3:
            return []
        # sort for dfs and checking duplicates
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
    def threeSum(self, numbers):
        result = []
        if numbers is None or len(numbers) < 3:
            return result
        numbers.sort()
        for i in xrange(len(numbers) - 2):
            # skip duplicates
            if i != 0 and numbers[i] == numbers[i-1]:
                continue
            left = i + 1
            right = len(numbers) - 1
            while left < right:
                sum = numbers[i] + numbers[left] + numbers[right]
                if sum == 0:
                    # list() needed? Seems no. [] acts as creating new list.
                    one_result = [numbers[i], numbers[left], numbers[right]]
                    result.append(one_result)
                    # update both pointers after getting one result
                    # or bug: right + 1 index out of range
                    left += 1
                    right -= 1
                    # skip duplicates after successfully have one result
                    while left < right and numbers[left] == numbers[left-1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right+1]:
                        right -= 1
                # sum < 0, meaning we need larger numbers, since it's sorted, left should advance
                elif sum < 0:
                    left += 1
                # sum > 0, we need smaller numbers, right should advance
                else:
                    right -= 1
        return result



numbers = [-1, 0, 1, 2, -1, -4]
Sol = Solution()
print Sol.threeSum(numbers)
