# hash33: http://www.lintcode.com/en/problem/hash-function/
# python: ord("c"), return ascii
# hash("abcd") = (a * 33^3 + b * 33^2 + c * 33 + d) % hashtable_size
# This is APR (Apache Portable Runtime) hash function

class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        ascii_list = [ord(c) for c in key]
        sum = 0
        for ascii in ascii_list:
            sum = sum * 33 + ascii
            sum = sum % HASH_SIZE
        return sum

Sol = Solution()
print Sol.hashCode("abcd", HASH_SIZE=100)
# print ord("c")