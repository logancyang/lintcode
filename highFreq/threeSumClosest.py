# threeSumClosest: http://www.lintcode.com/en/problem/3-sum-closest/

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        if numbers is None or len(numbers) == 0:
            return -1
        numbers.sort()
        result = -1
        min_dist = float("inf")
        for i in xrange(len(numbers)):
            a = numbers[i]
            # skip duplicates
            if i != 0 and numbers[i] == numbers[i-1]:
                continue
            start = i + 1
            end = len(numbers) - 1
            while start < end:
                tmp_sum = a + numbers[start] + numbers[end]
                if abs(tmp_sum-target) < min_dist:
                    min_dist = abs(tmp_sum-target)
                    result = tmp_sum
                if tmp_sum < target:
                    start += 1
                else:
                    end -= 1
        return result

A = [-1, 2, 1, -4]
target = 1
Sol = Solution()
print Sol.threeSumClosest(A, target)