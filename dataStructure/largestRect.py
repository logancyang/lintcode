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
        for i in xrange(len(height)+1):
            if i == len(height):
                current = -1
            else:
                current = height[i]

            while len(stack) != 0 and current <= height[stack[-1]]:
                h = height[stack.pop()]
                if len(stack) == 0:
                    w = i
                else:
                    w = i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)
            
        return max_area