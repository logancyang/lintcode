# heapify: http://www.lintcode.com/en/problem/heapify/
# Heapify an integer array into a min-heap array
# Heap has push(), pop(), top()


class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftdown(self, A, k):
        # all of siftdown is this while loop
        # k can be the smallest already and break
        # or k can be updated to its child, k * 2 + 1 or 2
        # each iteration heapifies the current triangle, and pass to the its subtree triangle and check again
        while k < len(A):
            smallest = k
            # compare kth node with its left child, mark the smallest
            if k * 2 + 1 < len(A) and A[k*2+1] < A[smallest]:
                smallest = k * 2 + 1
            # compare kth node with its left child, mark the smallest
            if k * 2 + 2 < len(A) and A[k*2+2] < A[smallest]:
                smallest = k * 2 + 2
            # if k is the smallest of the 3, do nothing
            if k == smallest:
                break
            # swap the kth and the smallest
            temp = A[smallest]
            A[smallest] = A[k]
            A[k] = temp
            # update k to its smaller child
            k = smallest

    def heapify(self, A):
        # starting from len(A)/2 and decrement
        # len(A)/2 is the lowest and last parent in the heap
        # check backward
        for i in xrange(len(A)/2, -1, -1):
            self.siftdown(A, i)

# print range(20, 10, -1)
