# removeDupListII: http://www.lintcode.com/problem/remove-duplicates-from-sorted-list-ii
# remove all numbers with duplicates

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
        if head is None or head.next is None:
            return head

        # dummy node is new head
        dummy = ListNode(None)
        # store the original head in dummy.next
        dummy.next = head
        # DO NOT USE head AGAIN!! IT IS NOW dummy.next
        node = dummy

        # while node.next.next is not None (the end). node starts at dummy
        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                value = node.next.val
                # skip the current node.next
                while node.next and node.next.val == value:
                    node.next = node.next.next
            else:
                # move node pointer forward 1 step
                node = node.next

        return dummy.next

