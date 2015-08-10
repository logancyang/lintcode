# levelOrder

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        queue = []
        queue.append(root)

        while len(queue) != 0:
            level = []
            # record the size of the current level
            size = len(queue)
            # traverse the current level
            for i in xrange(size):
                # use deque.popleft() for better efficiency
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
