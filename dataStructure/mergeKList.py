# mergeKList: http://www.lintcode.com/en/problem/merge-k-sorted-lists/

from heapq import *

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        