# single number: http://www.lintcode.com/en/problem/single-number/
# Use O(1) space, cannot use hashmap.
# Use xor ^: binary addition without advancing digit
# * a ^ a = 0;
# * a ^ 0 = a;
# a ^ b = b ^ a
# (a ^ b) ^ c = a ^ (b ^ c) 
# TODO: binary manipulation in ladder

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        if A is None or len(A) == 0:
            return 0
        n = A[0]
        for i in xrange(1, len(A)):
            # a same number will kill off a previous same number
            n = n ^ A[i]
        # After the loop, only the single number is left
        return n
