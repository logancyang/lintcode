# hIndex: https://leetcode.com/problems/h-index/
# h-Index: A scientist has index h, if h of his N papers have at least 
# h citations each, and the other N - h papers have no more than h citations each.
# citations = [3, 0, 6, 1, 5]
# N = 5 papers, 3 papers have at least 3

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        if len(citations) == 1:
            return min(citations[0], 1)
        citations.sort()
        max_index = max(citations)
        n_papers = len(citations)
        h_index = min(citations[0], n_papers)
        max_range = min(max_index+1, n_papers)
        for h in xrange(1, max_range):
            # min(citations[n-h:]) = citations[n-h]
            if n_papers-h-1 >= 0 and citations[n_papers-h] >= h and citations[n_papers-h-1] <= h:
                h_index = h
        return h_index

ci = [3, 0, 6, 1, 5]
Sol = Solution()
print Sol.hIndex(ci)