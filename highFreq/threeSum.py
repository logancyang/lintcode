# threeSum: http://www.lintcode.com/en/problem/3-sum/

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if numbers is None or len(numbers) == 0:
            return -1
        numbers.sort()
        result = []
        for i in xrange(len(numbers)):
            a = numbers[i]
            # skip duplicate numbers
            if i != 0 and numbers[i] == numbers[i-1]:
                continue
            # safely look only after i, previous results are added
            start = i + 1
            end = len(numbers) - 1
            while start < end:
                if numbers[start] + numbers[end] == -a:
                    local = [a, numbers[start], numbers[end]]
                    local.sort()
                    result.append(local)
                    start += 1
                    end -= 1
                    # skip duplicates
                    while start < end and numbers[start] == numbers[start-1]:
                        start += 1
                    while start < end and numbers[end] == numbers[end+1]:
                        end -= 1
                elif numbers[start] + numbers[end] < -a:
                    start += 1
                else:
                    end -= 1
        return result

A = [-1, 0, 1, 2, -1, -4]
Sol = Solution()
print Sol.threeSum(A)