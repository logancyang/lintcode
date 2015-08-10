"""
There are two sorted arrays A and B of size m and n respectively. 
Find the median of the two sorted arrays.

Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.
The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    # remember this recursive findKth() for two sorted arrays, useful
    def findKth(self, A, B, k):
        # recursion base case
        if len(A) == 0:
            return B[k-1]
        if len(B) == 0:
            return A[k-1]
        if k == 1:
            return min(A[0], B[0])

        a = A[k/2 - 1] if len(A) >= k/2 else None
        b = B[k/2 - 1] if len(B) >= k/2 else None

        # the case in which we throw A[:k/2-1] away
        if b is None or (a is not None and a < b):
            return self.findKth(A[k/2:], B, k - k/2)
        # the case in which we throw B[:k/2-1] away
        return self.findKth(A, B[k/2:], k - k/2)

    def findMedianSortedArrays(self, A, B):
        m = len(A) + len(B)
        # odd
        if m % 2 == 1:
            return self.findKth(A, B, m/2 + 1)
        # even
        else:
            bigger = self.findKth(A, B, m/2 + 1)
            smaller = self.findKth(A, B, m/2)
            return (bigger + smaller)/2.0