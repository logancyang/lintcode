"""
Strictly ascending 2D array
"""

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return False
        nrow = len(matrix)
        ncol = len(matrix[0])
        flatten = [x for sublist in matrix for x in sublist]
        start = 0
        end = len(flatten) - 1
        while start + 1 < end:
            mid = (start + end)/2
            if flatten[mid] == target:
                end = mid
            if flatten[mid] > target:
                end = mid
            if flatten[mid] < target:
                start = mid

        if flatten[start] == target:
            return True
        if flatten[end] == target:
            return True
        return False



