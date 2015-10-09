# gameOfLife: https://leetcode.com/problems/game-of-life/

"""
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell 
interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

- Any live cell with fewer than 2 live neighbors dies, as if caused by under-population.
- Any live cell with 2 or 3 live neighbors lives on to the next generation.
- Any live cell with more than 3 live neighbors dies, as if by over-population..
- Any dead cell with exactly 3 live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You 
cannot update some cells first and then use their updated values to update other cells.

We update the board in-place for the going-to-be-alive cells like this:

0 (0b00) dead | 2 (0b10) = 0b10
1 (0b01) alive | 2 (0b10) = 0b11

Update the board in-place is fine here since we can check for the previous dead/alive state using:
dead % 2 == 0, alive % 2 == 1

But when we want the updated version (for the living cells), simply do:
0b10 >> 1 = 1, 0b11 >> 1 = 1

Only update the dead -> live and live -> live ones, others are default to -> dead with >> operation.

2. In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches the border of the array. How would you 
address these problems?
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return
        # bug: copy 2D list, do not do list(2DList), do [list(row) for row in 2DList]
        # self.board_copy = [list(row) for row in board]
        self.neighbor_list = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                self.next_gen(board, x, y)
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                board[x][y] = (board[x][y] >> 1)
        return

    def next_gen(self, board, x, y):
        count_live = 0
        for direction in self.neighbor_list:
            new_x, new_y = x + direction[0], y + direction[1]
            if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
                continue
            if board[new_x][new_y] % 2 == 1:
                count_live += 1
        # the cell being checked is alive
        if board[x][y] % 2 == 1:
            if count_live == 2 or count_live == 3:
                board[x][y] |= 2
        # the cell is dead
        elif board[x][y] % 2 == 0:
            if count_live == 3:
                board[x][y] |= 2

Sol = Solution()
board = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
    ]

"""
Output:
[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
"""

Sol.gameOfLife(board)
print board

