# largestRect: http://www.lintcode.com/en/problem/largest-rectangle-in-histogram/

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        if height is None or len(height) == 0:
            return 0

        stack = []
        max_area = 0
        # i goes to len
        for i in xrange(len(height)+1):
            # i reaches len, all items pushed in, push -1 in to clear all in stack
            if i == len(height):
                current = -1
            else:
                current = height[i]
            # while stack not empty, and current <= stack top
            # stack top will be kicked out
            # each area calculation occurs at each pop
            while len(stack) != 0 and current <= height[stack[-1]]:
                # calculate the area for h, the popped out item
                # since we already knew its left smaller stack[-1] and right smaller i
                h = height[stack.pop()]
                # if after pop, stack empty, meaning it has no left smaller, w = i
                if len(stack) == 0:
                    w = i
                # after pop stack not empty, w = i - top - 1
                # the current top is the item after pop
                else:
                    w = i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area

H = [2, 1, 5, 6, 2, 3]
Sol = Solution()
print Sol.largestRectangleArea(H)