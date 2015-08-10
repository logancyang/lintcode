"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Example
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        if A is None or len(A) == 0:
            return 0
        if target > A[-1]:
            return len(A)
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end)/2
            #print start, end, mid
            if A[mid] >= target:
                end = mid
            if A[mid] < target:
                start = mid
        #print start, end
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return


A = [1,10,1001,201,1001,10001,10007]
target = 10008
Sol = Solution()
print Sol.searchInsert(A, target)