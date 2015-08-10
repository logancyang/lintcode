"""
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.

For the following binary search tree, in-order traversal by using 
iterator is [1, 6, 10, 11, 12]

   10
 /    \
1      11
 \       \
  6       12
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = Solution(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""

# equivalent to writing iterative in-order traversal
# iterative DFS: use stack
# at init(), push into stack from root to bottom left
# at next(), pop result, push into stack the left children of its
# right child
class Solution:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.stack = []
        while root is not None:
            self.stack.append(root)
            root = root.left

    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        if len(self.stack) != 0:
            return True
        return False

    #@return: return next node
    def next(self):
        # cmd + d select more occurrences
        current = self.stack.pop()
        result = current
        if current.right is not None:
            current = current.right
            while current is not None:
                self.stack.append(current)
                current = current.left
        return result
