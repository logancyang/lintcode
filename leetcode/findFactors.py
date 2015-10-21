# findFactors: find the prime factors of a number if the factors are in [2, 3, 5, 7, 11, 13, 17, 19]
# or return []

class Solution(object):
    def findFactors(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return []
        if num == 1:
            return [1]
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19]
        self.result = []
        path = []
        self.dfs(num, path)
        return self.result

    def dfs(self, num, path):
        # base
        if num == 1:
            self.result.append(list(path))
            return
        # recursion
        for prime in self.primes:
            if num % prime != 0:
                continue
            # avoid duplicates by making path ascending
            if path != [] and path[-1] > prime:
                continue
            new_num = num/prime
            path.append(prime)
            self.dfs(new_num, path)
            path.pop()
        return

n = 570
Sol = Solution()
print Sol.findFactors(n)






