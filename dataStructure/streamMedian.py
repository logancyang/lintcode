# data stream median: http://www.lintcode.com/en/problem/data-stream-median/
# NOTICE: in Python, heapq is a min-heap, to use a max-heap, push -item in.

from heapq import *

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        result = []
        if nums is None or len(nums) == 0:
            return result
        median = nums[0]
        max_heap = []
        min_heap = []
        result.append(median)
        for i in xrange(1, len(nums)):
            if nums[i] < median:
                # since heapq is min-heap, push in -item to have a max-heap
                heappush(max_heap, -nums[i])
            else:
                heappush(min_heap, nums[i])

            # left side too big
            if len(max_heap) > len(min_heap):
                heappush(min_heap, median)
                # don't forget - with max_heap
                median = -heappop(max_heap)
            # right side too big
            elif len(max_heap) + 1 < len(min_heap):
                # don't forget - with max_heap
                heappush(max_heap, -median)
                median = heappop(min_heap)
            result.append(median)
        return result


