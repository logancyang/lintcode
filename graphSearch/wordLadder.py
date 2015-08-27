# wordLadder: http://www.lintcode.com/en/problem/word-ladder/
# note: function chr(i) returns a char whose ASCII code is i.
# map(chr, range(97, 123)) returns a list from 'a' to 'z'
from collections import deque

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if dict is None or len(dict) == 0:
            return 0
        # hash: visited nodes
        hash = set([])
        queue = deque()
        hash.add(start)
        queue.append(start)

        length = 1
        while len(queue) != 0:
            # these two lines: when BFS # levels is needed
            length += 1
            size = len(queue)
            for i in xrange(size):
                word = queue.popleft()
                next_words = self.enumDistOneWords(word, dict)
                for next_word in next_words:
                    if next_word in hash:
                        continue
                    if next_word == end:
                        return length
                    hash.add(next_word)
                    queue.append(next_word)
        return 0

    def enumDistOneWords(self, word, dict):
        """Enumerate all words in dict that can be obtained by changing 
        one char in word. Return a list of these words"""
        result_set = set([])
        alphabets = map(chr, range(97, 123))
        for i in xrange(len(word)):
            new_word_list = list(word)
            for letter in alphabets:
                new_word_list[i] = letter
                new_word = ''.join(new_word_list)
                if new_word != word and new_word in dict:
                    result_set.add(new_word)
        return list(result_set)

start = "hit"
end = "cog"
dict1 = ["hot","dot","dog","lot","log", "cog"]
Sol = Solution()
nextwords = Sol.enumDistOneWords(start, dict1)
# print nextwords
print Sol.ladderLength(start, end, dict1)



