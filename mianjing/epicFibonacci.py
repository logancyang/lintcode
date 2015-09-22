# epicFibonacci:
# There is one kind of numbers call Fibbonaci Number, which satisfy the following situation: 
# A. can be spilt into several numbers;
# B. The first two numbers are the same, the next number is equal to the sum of previous two 
# eg. 112 (2 = 1 + 1), 12,122,436(12 + 12 = 24,12 + 24 = 36)
# If you are given a range by the user, find all numbers that are Fibbonaci numbers.
from math import *

class Solution:

    def fibonacci(self, my_range):
        """
        my_range: [left, right]
        """
        left = my_range[0]
        right = my_range[1]
        result = []
        components = [0] * 3
        max_range = int(sqrt(right))
        for i in xrange(1, max_range):
            components[0] = i
            components[1] = i
            components[2] = 2 * i
            concat = str(components[0]) + str(components[1]) + str(components[2])
            value = int(concat)
            while value <= right:
                if value >= left:
                    result.append(value)
                components[0] = components[1]
                components[1] = components[2]
                components[2] = components[0] + components[1]
                concat = concat + str(components[2])
                value = int(concat)
        return result

my_range = [1, 12122437]
Sol = Solution()
print Sol.fibonacci(my_range)