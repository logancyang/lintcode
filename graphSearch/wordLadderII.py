# wordLadderII: http://www.lintcode.com/en/problem/word-ladder-ii/

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        if start is None or end is None or len(start) != len(end):
            return []
        if start not in dict or end not in dict:
            return []
        # global var dict
        self.dict = dict
        # global var distance, a dict that records the distance from
        # the current word to end
        self.distance = {}
        # BFS to set self.distance for words
        self.BFS(end)
        # global var results
        self.results = []
        # DFS to enumerate the paths, add to global results
        if start in self.distance:
            self.DFS(start, end, [start])
        return self.results

    def BFS(self, end):
        # distance from end to end is 0
        self.distance[end] = 0
        # BFS queue
        queue = [end]
        while len(queue) != 0:
            head = queue[0]
            queue.pop(0)
            for word in self.getNextWords(head, self.dict):
                # a word that's one letter from end, and not visited
                if word not in self.distance:
                    self.distance[word] = self.distance[head] + 1
                    queue.append(word)

    def DFS(self, curr, target, path):
        # base case: current hits target, add this path to global results and return
        if curr == target:
            self.results.append(list(path))
            return
        # recurse down for each next word: curr = word, path appends word
        for word in self.getNextWords(curr, self.dict):
            # dict.get(key, defaultValueIfKeyDoesNotExist)
            if self.distance.get(word, -2) + 1 == self.distance[curr]:
                path.append(word)
                self.DFS(word, target, path)
                path.pop()

    def getNextWords(self, word, dict):
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
dict1 = ["hit", "hot", "dot", "dog", "lot", "log", "cog"]
Sol = Solution()
print Sol.findLadders(start, end, dict1)