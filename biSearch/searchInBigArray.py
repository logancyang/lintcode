# searchInBigArray: http://www.lintcode.com/en/problem/search-in-a-big-sorted-array/

class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, A, target):
        if A is None or len(A) == 0:
            return 0
        # let end be roughly k, to let the binary search be O(log k)
        end = 0
        while end < len(A) and A[end] < target:
            end = end * 2 + 1

        start = 0
        while start + 1 < end:
            mid = (start + end)/2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
