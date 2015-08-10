# isBalanced
from biTree import *

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        balanced, _ = self.checkDepth(root)
        return balanced

    def checkDepth(self, root):
        if root is None:
            return True, 0
        balanced, leftDepth = self.checkDepth(root.left)
        if not balanced:
            return False, 0
        balanced, rightDepth = self.checkDepth(root.right)
        if not balanced:
            return False, 0
        return abs(leftDepth-rightDepth) <= 1, max(leftDepth, rightDepth) + 1