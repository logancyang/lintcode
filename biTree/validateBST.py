# validateBST

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    # method 1: use the fact that BST's inorder traversal is sorted
    # O(n) space
    def isValidBST(self, root):
        result = self.inorder(root)
        prev = float("-inf")
        for item in result:
            if item <= prev:
                return False
            prev = item
        return True

    def inorder(self, root):
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.val)
            result.extend(self.inorder(root.right))
        return result

    # method 2: O(1) space
    def isValidBST(self, root):
        # set global var: prev
        self.prev = None
        return self.validBSThelper(root)

    def validBSThelper(self, root):
        if root is None:
            return True
        # check left subtree
        left = self.validBSThelper(root.left)
        if left is False:
            return False
        # check root, assign current root to prev
        if self.prev and root.val <= self.prev.val:
            return False
        self.prev = root
        # check right subtree
        right = self.validBSThelper(root.right)
        if right is False:
            return False
        return True