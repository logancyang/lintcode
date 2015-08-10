# postorder

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
    @return: postorder in list which contains node values.
    """
    ## non-recursive
    def postorderTraversal(self, root):
        stack = []
        result = []
        if root is None:
            return result
        # previously traversed node
        prev = None
        # current node
        node = root
        stack.append(root)
        while len(stack) != 0:
            node = stack[-1]
            # prev -> node was traversing down the tree
            if prev is None or prev.left == node or prev.right == node:
                if node.left:
                    stack.append(node.left)
                # only push in one node from left and right
                elif node.right:
                    stack.append(node.right)
            # prev -> node was traversing up the tree from left
            elif node.left == prev:
                if node.right:
                    stack.append(node.right)
            # prev -> node was traversing up the tree from right
            # in this case, we have added left and right
            # add root(current node) now
            else:
                result.append(node.val)
                stack.pop()
            prev = node
        return result

    ## recursive
    # def postorderTraversal(self, root):
        # result = []
        # if root:
        #     result.extend(self.postorderTraversal(root.left))
        #     result.extend(self.postorderTraversal(root.right))
        #     result.append(root.val)
        # return result

Sol = Solution()
print Sol.postorderTraversal(myBST.root)