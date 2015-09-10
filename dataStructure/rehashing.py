# rehashing: http://www.lintcode.com/en/problem/rehashing/


# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        if hashTable is None or len(hashTable) == 0:
            return []
        capacity = len(hashTable)
        keys = []
        for node in hashTable:
            while node and node.val:
                keys.append(node.val)
                node = node.next
        print keys
        size = len(keys)
        if size >= capacity/10:
            capacity *= 2
            new_hash = [ListNode(None) for i in xrange(capacity)]
            for key in keys:
                print key
                pos = key % capacity
                new_node = new_hash[pos]
                while new_node and new_node.val is not None:
                    new_node = new_node.next
                new_node = ListNode(key)
        return new_hash

Node_0 = ListNode(None)
Node_1 = ListNode(None)
Node_2 = ListNode(29)
Node_2.next = ListNode(5)
hashTable = [Node_0, Node_1, Node_2]
Sol = Solution()
result = Sol.rehashing(hashTable)
for item in result:
    while item:
        print item.val,
        item = item.next
    print