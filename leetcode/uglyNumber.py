# uglyNumber: https://leetcode.com/problems/ugly-number/

"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are 
ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        return self.dfs(num)

    def dfs(self, num):
        # base
        if num == 1:
            return True
        # recursion
        primes = [2, 3, 5]
        for prime in primes:
            if num % prime != 0:
                continue
            new_num = num/prime
            if self.dfs(new_num):
                return True
        return False

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        return self.dfs(num)

    def dfs(self, num):
        # base
        if num == 1:
            return True
        # recursion
        primes = [2, 3, 5]
        for prime in primes:
            if num % prime != 0:
                continue
            new_num = num/prime
            if self.dfs(new_num):
                return True
        return False

n = 20
Sol = Solution()
print Sol.isUgly(n)










