# LRUcache: http://www.lintcode.com/en/problem/lru-cache/
# 2 data structures used: a linked list, a hash map
# LRUCache_S version:
# linked list: head is dummy
# hash map: store the node's prev, hash[node.key] = node.prev, a node.key -> LinkedNode mapping

# singly-linked list + hash version
class LinkedNode:
    # different than ListNode in previous problems
    # has both key and value
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache_S:

    def __init__(self, capacity):
        self.hash = {}
        # head is a dummy
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    def push_back(self, node):
        # idea is hash[node.key] = node.prev
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    # change dummy (self.head) -> node -> next_node
    # to dummy -> next_node
    def pop_front(self):
        # del hash[head.next.key] = head
        del self.hash[self.head.next.key]
        # del head.next
        self.head.next = self.head.next.next
        # set hash[new head.next.key] = head
        self.hash[self.head.next.key] = self.head

    # change prev -> node -> next ... -> tail
    # to prev -> next ... -> tail -> node
    def move_to_tail(self, prev):
        node = prev.next
        if node == self.tail:
            return
        # del node
        prev.next = node.next
        # set hash[node.next] = prev
        if node.next:
            self.hash[node.next.key] = prev
            node.next = None
        # add node at tail
        self.push_back(node)

    def get(self, key):
        if key not in self.hash:
            return -1
        # see, hash is used to emulate .prev
        # and instantly get to that prev node
        self.move_to_tail(self.hash[key])
        # return the VALUE of the key node
        # we can only get to prev instantly, not the key node
        return self.hash[key].next.value

    def set(self, key, value):
        if key in self.hash:
            self.move_to_tail(self.hash[key])
            # set the new value on the old node
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()


# doubly-linked list + hash version
class DoubleLinkedNode:
    # don't need hash[node.key] = node.prev
    # instead use hash[node.key] = node
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache_D:

    def __init__(self, capacity):
        self.hash = {}
        # head is a dummy
        self.head = DoubleLinkedNode()
        self.tail = self.head
        self.capacity = capacity

    def push_back(self, node):
        # idea is hash[node.key] = node.prev
        self.hash[node.key] = node
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    # change dummy (self.head) -> node -> next_node
    # to dummy -> next_node
    def pop_front(self):
        # del hash[head.next.key] = head.next
        del self.hash[self.head.next.key]
        # del head.next
        next_node = self.head.next.next
        self.head.next = next_node
        next_node.prev = self.head
        # set hash[new head.next.key] = head.next
        self.hash[self.head.next.key] = self.head.next

    # change prev -> node -> next ... -> tail
    # to prev -> next ... -> tail -> node
    def move_to_tail(self, node):
        if node == self.tail:
            return
        # del node
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        # add node at tail
        self.push_back(node)

    def get(self, key):
        if key not in self.hash:
            return -1
        # instantly get to node from node.key
        self.move_to_tail(self.hash[key])
        # return the VALUE of the key node
        return self.hash[key].value

    def set(self, key, value):
        if key in self.hash:
            self.move_to_tail(self.hash[key])
            # set the new value on the old node
            self.hash[key].value = value
        else:
            self.push_back(DoubleLinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()



# a_none_node = None
# if a_none_node:
#     print "oh no!"
# else:
#     print "no problem!"   # no problem :)



