# singlenumberII: http://www.lintcode.com/en/problem/single-number-ii/
# 3n+1 numbers, all occurs 3 times except one (occurred once). Find it.
# Adopt the idea of single number I.
# Find an operation x that satisfies:
# a x a x a = 0
# Idea: ternary addition without advancing digit

class Solution:
    """
    @param A : An integer array
    @return : An integer
    """
    def singleNumberII(self, A):
        if A is None or len(A) == 0:
            return -1

        bits = [0] * 20
        # note: not really convert to base3 number
        # it accumulates remainders of each of the 20 bits, for each number in A
        # the accumulated "base3" digits can be bigger than 3 at each bit
        # because our operation is addition with no advancing digit, 
        # we can treat each digit separately
        for i in xrange(20):
            # for a fixed bit, compute the bit in base3 for numbers in A
            for j in xrange(len(A)):
                bits[i] += A[j] / (3**i) % 3  

        # convert the "base 3" accumulated number 
        # (it already is the result if converted to real base3 number) to decimal
        result = 0
        for i in xrange(20):
            # (bits[i] % 3) convert the accumulated number to real ternary number
            result += (3**i) * (bits[i] % 3)
        return result


A = [1,1,2,3,3,3,2,2,4,1]
Sol = Solution()
print Sol.singleNumberII(A)

