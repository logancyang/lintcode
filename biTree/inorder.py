# inorder
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
    @return: Inorder in list which contains node values.
    """
    ## non-recursive
    def inorderTraversal(self, root):
        stack = []
        result = []
        if root is None:
            return result

        node = root
        # check both conditions: stack empty or not, node None or not
        # if stack is empty, but node is not, the while node loop makes sure
        # the current node is pushed into stack, so there's something to pop.
        while len(stack) != 0 or node:
            # while node is not None, push it to stack
            # keep traversing to left child
            # the leftmost remaining node is always on top of the stack
            while node:
                stack.append(node)
                node = node.left
            # add top stack node to result
            # traverse to right child
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result

    ## recursive
    # def inorderTraversal(self, root):
    #     result = []
    #     if root:
    #         result.extend(self.inorderTraversal(root.left))
    #         result.append(root.val)
    #         result.extend(self.inorderTraversal(root.right))
    #     return result


Sol = Solution()
print Sol.inorderTraversal(myBST.root)