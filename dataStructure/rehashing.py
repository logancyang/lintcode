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
        new_capacity = len(hashTable) * 2
        new_table = [None] * new_capacity

        for i in xrange(len(hashTable)):
            while hashTable[i]:
                new_index = (hashTable[i].val % new_capacity + new_capacity) % new_capacity
                if new_table[new_index] is None:
                    new_table[new_index] = ListNode(hashTable[i].val)
                else:
                    dummy = new_table[new_index]
                    while dummy.next:
                        dummy = dummy.next
                    dummy.next = ListNode(hashTable[i].val)
                hashTable[i] = hashTable[i].next
        return new_table

# Node_0 = ListNode(None)
# Node_1 = ListNode(None)
# Node_2 = ListNode(29)
# Node_2.next = ListNode(5)
# hashTable = [Node_0, Node_1, Node_2]
# Sol = Solution()
# result = Sol.rehashing(hashTable)
# print result

    # def rehashing(self, hashTable):
    #     if hashTable is None or len(hashTable) == 0:
    #         return []
    #     new_capacity = len(hashTable) * 2
    #     keys = []
    #     for node in hashTable:
    #         while node and node.val:
    #             keys.append(node.val)
    #             node = node.next
    #     new_hashTable = [None for i in xrange(new_capacity)]
    #     for key in keys:
    #         pos = key % new_capacity

    #         prev = None
    #         current = new_hashTable[pos]
            
    #         if new_hashTable[pos] is None:
    #             new_hashTable[pos] = ListNode(key)
                
    #         while current:
    #             prev = current
    #             current = current.next
                
    #         current = ListNode(key)
    #         if prev:
    #             prev.next = current
    #     return new_hashTable

# assignment is not actual reference
# if need to change element in list, use list method in place
# A = [1, 2, 3]
# a = A[2]
# print a
# A[2] = 1
# print A