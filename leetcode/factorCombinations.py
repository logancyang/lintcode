__author__ = 'loganyang'

# factorCombinations:

"""
Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:
- Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
- n > 0
- 1 < Factors < n.

Examples:
    input: 1
        output: []
    input: 37
        output: []
    input: 12
        output:
        [[2, 6],  [2, 2, 3],  [3, 4]]
    input: 32
        output:
        [[2, 16],  [2, 2, 8],  [2, 2, 2, 4],  [2, 2, 2, 2, 2],  [2, 4, 4],  [4, 8]]

Method: DFS from large factors to small ones
"""

class Solution:

    def factors(self, n):
        self.result = []
        if n <= 1:
            return self.result
        path = []
        self.dfs(n, path)
        return self.result

    def dfs(self, n, path):
        # base case
        # len(path) == 1 is the case [n], which is not included in this question
        if n == 1 and len(path) > 1:
            self.result.append(list(path))
            return
        # recursion
        # factor must include n itself
        # or when it's down to the last factor, it's not added
        for factor in xrange(2, n+1):
            # check if it's a factor of not
            if n % factor != 0:
                continue
            # ensure ascending order
            if path == [] or path[-1] <= factor:
                path.append(factor)
                self.dfs(n/factor, path)
                path.pop()
        return

Sol = Solution()
n = 32
print Sol.factors(n)


# checking for whole number
# print 5.0 % 1
# print 0.0 == 0
# print 5.5 % 1
# or
# print (5.0).is_integer()
# print (5.5).is_integer()





