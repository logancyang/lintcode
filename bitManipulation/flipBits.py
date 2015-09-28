# flip bits: http://www.lintcode.com/en/problem/flip-bits/
# Hamming distance: https://en.wikipedia.org/wiki/Hamming_weight


class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    # for positives
    def bitSwapRequiredPos(self, a, b):
        n = a ^ b
        count = 0
        # for positive n
        while n > 0:
            count += 1
            n = n & (n - 1)
        return count

    def bitSwapRequired(self, a, b):
        str_a = self.toBinString32(a)
        str_b = self.toBinString32(b)
        count = 0
        for i in xrange(32):
            if str_a[i] != str_b[i]:
                count += 1
        return count

    def toBinString32(self, a):
        """
        convert decimal to 32-bit Two's Complement form
        """
        if a >= 0:
            str_a = bin(a)[2:]
            len_a = len(str_a)
            len_fill = 32
            return str_a.zfill(len_fill)
        else:
            mask32 = int('0b' + '1' * 32, 2)
            str_a = bin(a & mask32)[2:]
            len_fill = 32
            return str_a.zfill(len_fill)

# raw_input() outputs string
# run SublimeREPL Python Run Current File
a = 1
b = -1
Sol = Solution()
print Sol.bitSwapRequired(a, b)

## NOTE: how to use raw_input to input a list
# lst = raw_input("enter your list: ")
# print lst
# print type(lst)
# lst = eval(lst)
# print lst
# print type(lst)