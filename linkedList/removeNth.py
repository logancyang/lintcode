# removeNth: http://www.lintcode.com/en/problem/remove-nth-node-from-end-of-list/
from LinkedList import *

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if head is None or n <= 0:
            return
        dummy = ListNode(0)
        dummy.next = head
        count = 1
        prev_target = dummy
        while head.next:
            head = head.next
            count += 1
            if count > n:
                prev_target = prev_target.next
        if count == n:
            return prev_target.next.next
        if count < n:
            return dummy.next
        prev_target.next = prev_target.next.next
        return dummy.next