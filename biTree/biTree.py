__author__ = 'loganyang'

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BiTree:
    def __init__(self, root=None):
        self.root = root

    def BT2list(self, root):
        result = []
        if root:
            result.append(" (")
            result.extend(str(self.BT2list(root.left)))
            result.append(str(root.val))
            result.extend(str(self.BT2list(root.right)))
            result.append(") ")
        return ''.join(result)

# BST is a subclass of BiTree
class BinarySearchTree(BiTree):
    def insertNode(self, root, node):
        if root is None:
            root = node
            return root
        if node.val < root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root

    # for deletion. find the min node in a subtree
    def find_min(self, node):
        if node:
            while node.left:
                node = node.left
        return node

    def removeNode(self, root, value): # note: this method, root in, root out, return var same as input
        if root:
            if value < root.val:
                root.left = self.removeNode(root.left, value) # note: root.left = ..., not root
            elif value > root.val:
                root.right = self.removeNode(root.right, value)
            else: # delete in this block, value == root.val, now
                if root.left and root.right:
                    successor = self.find_min(root.right)
                    root.val = successor.val
                    root.right = self.removeNode(root.right, root.val)
                elif root.left is None:
                    root = root.right
                elif root.right is None:
                    root = root.left
        return root

myBST = BinarySearchTree()
myNode_1 = TreeNode(1)
myNode_2 = TreeNode(2)
myNode_3 = TreeNode(3)
myNode_4 = TreeNode(4)
myNode_5 = TreeNode(5)
myNode_6 = TreeNode(6)
myNode_7 = TreeNode(7)
myBST.root = myBST.insertNode(myBST.root, myNode_2)
myBST.root = myBST.insertNode(myBST.root, myNode_1)
myBST.root = myBST.insertNode(myBST.root, myNode_3)
myBST.root = myBST.insertNode(myBST.root, myNode_5)
myBST.root = myBST.insertNode(myBST.root, myNode_6)
myBST.root = myBST.insertNode(myBST.root, myNode_4)
"""
     2
    / \
   1   3
        \
         5
        / \
       4   6
"""
# print myBST.BT2list(myBST.root)
"""
myBT:

     1
    / \
   2   3
  / \   \
 4   9   5
        / \
       6   7
      /
     8
"""

Node_1 = TreeNode(1)
Node_2 = TreeNode(2)
Node_3 = TreeNode(3)
Node_4 = TreeNode(4)
Node_5 = TreeNode(5)
Node_6 = TreeNode(6)
Node_7 = TreeNode(7)
Node_8 = TreeNode(8)
Node_9 = TreeNode(9)

myBT = BiTree(Node_1)
Node_1.left = Node_2
Node_1.right = Node_3
Node_3.right = Node_5
Node_2.left = Node_4
Node_2.right = Node_9
Node_5.left = Node_6
Node_5.right = Node_7
Node_6.left = Node_8