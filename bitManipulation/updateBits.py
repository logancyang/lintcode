# updateBits: http://www.lintcode.com/en/problem/update-bits/
from toBinStringN import *


class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBitsN(self, n, m, i, j):
        if j < 31:
            mask = ~((1 << (j + 1)) - (1 << i))
        else:
            mask = (1 << i) - 1
        return (m << i) + (mask & n)

    def updateBits(self, n, m, i, j):
        if j > 31:
            j = 31
        str_n = toBinStringN(n, 32)
        str_m = toBinStringN(m, 32)
        list_n = list(str_n)[::-1]
        list_m = list(str_m)[::-1]
        ind_m = 0
        for ind in xrange(i, j+1):
            list_n[ind] = list_m[ind_m]
            ind_m += 1
        if ind_m < j - i - 1:
            list_n.extend(list_m[ind_m:])
        res_list = list_n[::-1]
        res = "".join(res_list)
        return int(res, 2)


n = 0b10000000000
m = 0b10101
i = 2
j = 6
Sol = Solution()
res = Sol.updateBits(n, m, i, j)
print res
