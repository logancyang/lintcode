# validSudoku: https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]], 9x9
        :rtype: bool
        """
        # check rows
        for i in xrange(9):
            if board[i].count('.') + len(set(board[i])) - 1 != 9:
                return False
        # check cols
        for j in xrange(9):
            col = [board[i][j] for i in xrange(9)]
            if col.count('.') + len(set(col)) - 1 != 9:
                return False
        # check 3x3 squares, xrange(0, 7, 3) = (0, 3, 6)
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[i+m][j+n] for m in xrange(3) for n in xrange(3)]
                if square.count('.') + len(set(square)) - 1 != 9:
                    return False
        return True