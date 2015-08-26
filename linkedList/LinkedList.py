__author__ = 'loganyang'

class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def list_print(self):
        node = self
        while node:
            print node.val,
            node = node.next
        print ""

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def add_node(self, val):
        # create a new node
        new_node = ListNode()
        new_node.val = val
        # link the new node to the 'previous' head.
        new_node.next = self.head
        # set the new head to the new node.
        self.head = new_node

    def list_print(self):
        node = self.head
        while node:
            print node.val,
            node = node.next
        print ""


S = [1]
myList = LinkedList()
for i in xrange(len(S)):
    myList.add_node(S[i])