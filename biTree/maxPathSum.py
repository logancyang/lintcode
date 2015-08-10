# maxPathSum
from biTree import *

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        max_any, _ = self.helper(root)
        return max_any

    def helper(self, root):
        if root is None:
            # max_any for the base case is -inf
            # because the values can be all negative
            return float("-inf"), 0
        # divide
        left_any, left_single = self.helper(root.left)
        right_any, right_single = self.helper(root.right)
        # conquer
        max_any = max(left_any, right_any, left_single + right_single + root.val)
        max_single = max(left_single + root.val, right_single + root.val, 0)
        return max_any, max_single