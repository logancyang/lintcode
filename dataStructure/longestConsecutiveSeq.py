# longestConsecutiveSeq: http://www.lintcode.com/en/problem/longest-consecutive-sequence/

class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # use a dict as a hashset
        # bug: do not use set([]), it's not iterable
        hash = {}
        for number in num:
            hash[number] = True

        max_con = 0
        for i in xrange(len(num)):
            # find the biggest consecutive number for num[i]
            top = num[i]
            # bug: do not use set([]) for hash, it's not iterable
            while top in hash:
                del hash[top]
                top += 1
            # find the smallest consecutive number for num[i]
            bottom = num[i] - 1
            while bottom in hash:
                del hash[bottom]
                bottom -= 1
            # update the longest consecutive
            if top - bottom - 1 > max_con:
                max_con = top - bottom - 1

        return max_con