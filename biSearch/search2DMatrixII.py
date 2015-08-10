class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        i = len(matrix) - 1
        j = 0
        count = 0
        while i >= 0 and j < len(matrix[0]):
            # use if, elif, else! DO NOT use if if if
            # though they are mutual exclusive
            # indices change and in the same iteration they all execute!
            if matrix[i][j] == target:
                count += 1
                i -= 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return count

mat = [[2, 3, 6], [3, 5, 7], [4, 5, 8]]
Sol = Solution()
print Sol.searchMatrix(mat, 3)
# print [item for sublist in mat for item in sublist]