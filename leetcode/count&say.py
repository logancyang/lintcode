# count&say: https://leetcode.com/problems/count-and-say/

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int, 0-based
        :rtype: str
        """
        if n is None or n < 1:
            return
        next = "1"
        # n-1 because nth is 1-based
        for i in xrange(n-1):
            next = self.convert(next)
        return next

    def convert(self, num):
        """
        num: string of a number
        return: convert to count-and-say form
        """
        if len(num) == 1:
            return "1" + num[0]
        candidate = num[0]
        count = 1
        result = ""
        for i in xrange(1, len(num)):
            if num[i] == num[i-1]:
                count += 1
            else:
                # different, add prev count&candidate to result
                result += str(count) + candidate
                candidate = num[i]
                count = 1
        # add the last candidate's result
        result += str(count) + candidate
        return result

n = 7
Sol = Solution()
print Sol.countAndSay(n)