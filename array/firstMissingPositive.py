# firstMissingPositive: http://www.lintcode.com/en/problem/first-missing-positive/

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if A is None or len(A) == 0:
            return 1
        pos_set = set(A)
        min_pos = float("inf")
        for num in A:
            minus = num - 1
            if minus > 0 and minus not in pos_set and minus < min_pos:
                min_pos = minus
                continue
            plus = num + 1
            if plus > 0 and plus not in pos_set and plus < min_pos:
                min_pos = plus
        if min_pos == float("inf"):
            return 1
        return min_pos

A = [1, 2, 0]
A = [3, 4, -1, 1]
Sol = Solution()
print Sol.firstMissingPositive(A)