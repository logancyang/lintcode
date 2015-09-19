# singlenumberIII: http://www.lintcode.com/en/problem/single-number-iii/

class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        if A is None or len(A) == 0:
            return -1
        # the group xor accumulator with single number a or b
        group_a = 0
        group_b = 0
        # xor the whole list
        xor = 0
        for i in xrange(len(A)):
            xor ^= A[i]
        # find the bit that's different
        # BUG: - has higher priority than &, add ()
        last_bit = xor - (xor & (xor - 1))
        # group A by that bit = 0 or 1
        for i in xrange(len(A)):
            # that bit is 0 in A[i]
            if A[i] & last_bit == 0:
                group_a ^= A[i]
            # that bit both 1
            else:
                group_b ^= A[i]

        return [group_a, group_b]

A = [1, 2, 2, 3, 4, 4, 5, 3]
Sol = Solution()
print Sol.singleNumberIII(A)