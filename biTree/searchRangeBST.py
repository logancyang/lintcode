# searchRangeBST

class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    # use inorder traversal, add left, root, right in order
    # to have ascending order in the result
    def searchRange(self, root, k1, k2):
        result = []
        if root is None:
            return result
        # a list of all keys in the left subtree
        result = self.searchRange(root.left, k1, k2)
        # append the current root value
        if k1 <= root.val <= k2:
            result.append(root.val)
        # a list of all keys in the right subtree
        right = self.searchRange(root.right, k1, k2)
        result.extend(right)
        return result
