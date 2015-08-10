# recursive preorder
from biTree import *

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    ## non-recursive, stack for DFS
    def preorderTraversal(self, root):
        stack = []
        result = []
        if root is None:
            return result
        
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            # push node.right in first for preorder
            # because LIFO, we want node.left to be popped first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    ## Divide & Conquer
    # def preorderTraversal(self, root):
    #     # write your code here
    #     result = []
    #     if root:
    #         result.append(root.val)
    #         result.extend(self.preorderTraversal(root.left))
    #         result.extend(self.preorderTraversal(root.right))
    #     return result

    ## traversal
    # def traverse(self, root, result):
    #     if root is None:
    #         return
    #     result.append(root.val)
    #     self.traverse(root.left, result)
    #     self.traverse(root.right, result)

    # def preorderTraversal(self, root):
    #     # write your code here
    #     result = []
    #     self.traverse(root, result)
    #     return result



Sol = Solution()
print Sol.preorderTraversal(myBST.root)