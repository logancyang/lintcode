# removeDupList: http://www.lintcode.com/problem/remove-duplicates-from-sorted-list
# remove all duplicates

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if head is None:
            return None
        # node pointer starting from head
        node = head
        # while node.next is not None (the end)
        while node.next:
            if node.val == node.next.val:
                # skip the current node.next
                node.next = node.next.next
            else:
                # move node pointer forward 1 step
                node = node.next

        return head