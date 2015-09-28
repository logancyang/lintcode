# twoSumClosest

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find the two numbers whose sum is closest to target
    """
    def twoSum(self, numbers, target):
        numbers.sort()
        start = 0
        end = len(numbers) - 1
        min_dist = float("inf")
        while start < end:
            tmp_sum = numbers[start] + numbers[end]
            if abs(tmp_sum - target) < min_dist:
                min_dist = abs(tmp_sum - target)
                result = [numbers[start], numbers[end]]
            if tmp_sum < target:
                start += 1
            else:
                end -= 1
        return result


A = [1, 3, 7, 9, 11]
target = 15
Sol = Solution()
print Sol.twoSum(A, target)