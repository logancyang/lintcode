# lca, no parent pointer
import copy
from biTree from *


class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # base case
        if root is None or root == A or root == B:
            return root

        # Divide
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        # Conquer
        # case 1: A, B in different subtrees, root is lca
        if left and right:
            return root
        # case 2: only one subtree has A and B
        if left:
            return left
        if right:
            return right
        # case 3: A, B not in this tree
        return