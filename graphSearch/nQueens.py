# nQueens: http://www.lintcode.com/en/problem/n-queens/
# for nQueensII, just return len(self.results)

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens, n*n chessboard
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        if n <= 0 or n is None:
            return []

        self.results = []
        ind_y = []
        self.dfs(n, ind_y)
        boards = [self.buildBoard(n, ind_y) for ind_y in self.results]
        return boards

    def dfs(self, n, ind_y):
        # base case
        if len(ind_y) == n:
            # bug: DO NOT FORGET TO NEW LIST()
            self.results.append(list(ind_y))

        # appending to ind_y results in a new row
        # so do not worry about keeping row indices, only loop y and
        # check against existing ind_y passed in
        for y in xrange(n):
            if not self.isValid(ind_y, y):
                continue
            ind_y.append(y)
            self.dfs(n, ind_y)
            ind_y.pop()

    def isValid(self, ind_y, new_y):
        """
        ind_y: list of y indices of old queens, start from 0 to n-1, order is row # x
        y: the new queen's y coordinate
        """
        # # of existing rows, also index of the new row
        new_x = len(ind_y)
        for old_x in xrange(new_x):
            # same column. (we don't consider same row, since we never add queen in the same row)
            if new_y == ind_y[old_x]:
                return False
            # same diag from top-left to bottom-right
            if new_x - new_y == old_x - ind_y[old_x]:
                return False
            # same diag from top-right to bottom-left
            if new_x + new_y == old_x + ind_y[old_x]:
                return False
        return True

    def buildBoard(self, n, ind_y):
        """
        n: length of board
        ind_y: list of y indices of the queens, start from 0 to n-1, order is row # x
        """
        line_list = ["."] * n
        board = []
        for i in xrange(n):
            cur_line_list = list(line_list)
            cur_line_list[ind_y[i]] = "Q"
            cur_line = "".join(cur_line_list)
            board.append(cur_line)
        return board

Sol = Solution()
print Sol.solveNQueens(5)

# Note: Python assign by reference, change b, a is changed. Must new list b = list(a)
# a = [1,1,2]
# b = a
# b[1] = 2
# print a -> [1,2,2]