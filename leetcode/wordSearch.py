# wordSearch: https://leetcode.com/problems/word-search/
# The question's input example is wrong. Input should be list of strings,
# not list of list of strings.


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return True

        my_board = [list(string) for string in board]
        # visited entries in board are set to None
        len_row = len(board[0])
        len_col = len(board)
        for y in xrange(len_row):
            for x in xrange(len_col):
                if self.dfs(my_board, word, x, y):
                    return True
        return False

    def dfs(self, board, word, x, y):
        if len(word) == 0:
            return True
        len_row = len(board[0])
        len_col = len(board)
        new_word = word[1:]
        if x < 0 or y < 0:
            return False
        if x >= len_col or y >= len_row:
            return False

        if board[x][y] == word[0]:
            board[x][y] = None
            if self.dfs(board, new_word, x, y+1):
                return True

            if self.dfs(board, new_word, x, y-1):
                return True

            if self.dfs(board, new_word, x+1, y):
                return True

            if self.dfs(board, new_word, x-1, y):
                return True
            board[x][y] = word[0]
        return False
board = [
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "CCBC"
Sol = Solution()

print Sol.exist(board, word)