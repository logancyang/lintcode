# maxtree: http://www.lintcode.com/en/problem/max-tree/


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        stack = []
        root = None
        for i in xrange(len(A)+1):
            right = TreeNode(float("inf")) if i == len(A) else TreeNode(A[i])

            while len(stack) != 0:
                if right.val > stack[-1].val:
                    popNode = stack.pop()
                    if len(stack) == 0:
                        right.left = popNode
                    else:
                        left = stack[-1]
                        if left.val > right.val:
                            right.left = popNode
                        else:
                            left.right = popNode
                else:
                    break
            stack.append(right)

        return stack[-1].left