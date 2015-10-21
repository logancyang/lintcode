# inorderSuccessorBST: http://www.lintcode.com/problem/inorder-successor-in-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        successor = None
        if root is None:
            return root
        # root > p: recurse left, set successor
        # root < p: recurse right, don't move successor
        while root and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        if root.right is None:
            return successor

        root = root.right
        while root.left:
            root = root.left

        return root
