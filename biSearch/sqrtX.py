# sqrtX: http://www.lintcode.com/en/problem/sqrtx/

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # bug: 1 is a special case
        if x == 1:
            return 1
        start = 0
        end = x
        while start + 1 < end:
            mid = (start + end)/2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                start = mid
            else:
                end = mid
        return start

x = 10
Sol = Solution()
print Sol.sqrt(x)
