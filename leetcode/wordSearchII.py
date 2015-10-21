# wordSearchII: https://leetcode.com/problems/word-search-ii/

class TrieNode(object):
    def __init__(self, string=None, is_end=False):
        self.string = string
        # maps an edge, child_char -> child_node
        self.dict = {}
        self.is_end = is_end

    def __str__(self):
        result = self.string
        if self.dict.keys() is None:
            return result
        result += " connected to: "
        for char in self.dict:
            result += char + ", "
        return result
    
    def get_string(self):
        return self.string

    def get_dict(self):
        return self.dict

    def set_next(self, child_char, child_node):
        """
        set the edge from this TrieNode to child_node
        """
        self.dict[child_char] = child_node

    def get_next(self, child_char):
        """
        return the child_node by child_char
        """
        if child_char in self.dict:
            return self.dict[child_char]
        return

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if word is None or len(word) == 0:
            pass
        prev_node = self.root
        for i in xrange(len(word)):
            node_string = word[:i+1]
            if prev_node.get_next(word[i]) is None:
                curr_node = TrieNode(node_string)
                prev_node.set_next(word[i], curr_node)
            else:
                curr_node = prev_node.get_next(word[i])
            prev_node = curr_node
        curr_node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return False
        node = self.root
        for char in word:
            if not node.get_next(char):
                return False
            node = node.get_next(char)
        return node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix is None or len(prefix) == 0:
            return True
        node = self.root
        for char in prefix:
            if not node.get_next(char):
                return False
            node = node.get_next(char)
        return True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[str]
        :type words: List[str]
        :rtype: List[str]
        """
        if words is None or len(words) == 0:
            return []
        result = []
        for word in words:
            if self.exist(board, word):
                result.append(word)
        return result
    
    def exist(self, board, word):
        """
        :type board: List[str]
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return True

        my_board = [list(string) for string in board]
        # visited entries in board are set to None
        len_row = len(board[0])
        len_col = len(board)
        path = ""
        # each (x, y) as start point
        for y in xrange(len_row):
            for x in xrange(len_col):
                if self.dfs(my_board, word, path, x, y):
                    return True
        return False

    def dfs(self, board, word, path, x, y):
        # base case
        if path == word:
            return True

        len_row = len(board[0])
        len_col = len(board)
        
        # index out of range, then failed
        if x < 0 or y < 0:
            return False
        if x >= len_col or y >= len_row:
            return False

        if board[x][y] == word[len(path)]:
            # set visited to None
            board[x][y] = None
            new_path = path + board[x][y]
            if self.dfs(board, word, new_path, x, y+1):
                return True

            if self.dfs(board, word, new_path, x, y-1):
                return True

            if self.dfs(board, word, new_path, x+1, y):
                return True

            if self.dfs(board, word, new_path, x-1, y):
                return True
            # don't forget to set visited slot back to original char after the dfs's
            board[x][y] = word[len(path)]
        return False

print "word"[::-1]