# happyNumber: https://leetcode.com/problems/happy-number/

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number 
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those 
numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        square_sum = 0
        square_sum_set = set()
        number = n
        while square_sum != 1:
            # get each digit
            digits = self.get_digits(number)
            square_sum = sum(digit**2 for digit in digits)
            if square_sum == 1:
                return True
            if square_sum in square_sum_set:
                return False
            else:
                square_sum_set.add(square_sum)
            number = square_sum

        return False

    def get_digits(self, number):
        digits = []
        while number > 0:
            remainder = number % 10
            digits.append(remainder)
            number /= 10
        return digits



n = 19
Sol = Solution()
print Sol.isHappy(n)










