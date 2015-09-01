# woodCut: http://www.lintcode.com/en/problem/wood-cut/
# Get k or more equal-length pieces from L[i]
# What's the max length pf the pieces for a fixed k


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer, # of equal length pieces
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        if sum(L) < k:
            return 0
        maxlen = max(L)
        # search target length of the pieces
        start = 1
        end = maxlen
        while start + 1 < end:
            mid = (start + end)/2
            # mid is the equal-length we want
            # l/mid is the # of pieces we can get from l
            # pieces is the # of pieces we can get from L
            pieces = sum([l/mid for l in L])
            # pieces >= k, meaning we might be able to get longer pieces
            # bug: >=, not >
            if pieces >= k:
                start = mid
            else:
                end = mid

        if sum([l/end for l in L]) >= k:
            return end
        return start