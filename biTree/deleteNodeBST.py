# deleteNodeBST


class Solution:
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """    
    def find_min(self, node):
        if node:
            while node.left:
                node = node.left
        return node

    # note: this method, root in, root out, return var same as input
    # root is just the representation of the whole tree
    def removeNode(self, root, value): 
        if root:
            if value < root.val:
                root.left = self.removeNode(root.left, value) # note: root.left = ..., not root
            elif value > root.val:
                root.right = self.removeNode(root.right, value)
            # delete in this block, value == root.val, now
            else:
                # root has both children
                if root.left and root.right:
                    successor = self.find_min(root.right)
                    # overwrite root.val with the min node from right subtree
                    root.val = successor.val
                    # recurse to modify the right subtree: remove its original min node
                    root.right = self.removeNode(root.right, root.val)
                # root has right child
                elif root.left is None:
                    root = root.right
                # root has left child
                elif root.right is None:
                    root = root.left
        return root