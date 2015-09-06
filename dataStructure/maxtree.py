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
        # a decreasing stack, while new > old, pop old
        # an item i's left is its 1st bigger to the left
        # the item that kicks i out is i's 1st bigger to the right
        stack = []
        root = None
        for i in xrange(len(A)+1):
            # use inf to kick out all elements in stack
            root = TreeNode(float("inf")) if i == len(A) else TreeNode(A[i])

            while len(stack) != 0:
                # [.., left, popNode], current
                # if current > popNode, current is popNode's 1st bigger to right
                if root.val > stack[-1].val:
                    popNode = stack.pop()
                    # stack empty, meaning it has no bigger to the left
                    # popNode is the left child of current
                    if len(stack) == 0:
                        root.left = popNode
                    else:
                        left = stack[-1]
                        # new top: left, if bigger than current, left > popNode < root
                        # where left is biggest. left is popNode's first bigger to left
                        # popNode is the smaller in the two's child
                        # if left > root, popNode is root's left child since root is on its right
                        if left.val > root.val:
                            root.left = popNode
                        # if root > left, popNode is left's right child
                        else:
                            left.right = popNode
                else:
                    break
            stack.append(root)

        return stack[-1].left