# sortColorsII: http://www.lintcode.com/en/problem/sort-colors-ii/

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # init a list for counting
        slots = [0] * k
        # count a hist
        for i in xrange(len(colors)):
            slots[colors[i] - 1] += 1
        # unfold the slots to a new array, ordered by slots values
        result = []
        for i in xrange(k):
            for j in xrange(slots[i]):
                result.append(i+1)
        return result

A = [2,1,1,2,2]
Sol = Solution()
print Sol.sortColors2(A, 2)