# twoSum: http://www.lintcode.com/en/problem/2-sum/

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if numbers is None or len(numbers) <= 1:
            return []
        map = {numbers[0]: 0}
        result = []
        for i in xrange(len(numbers)):
            if target - numbers[i] in map:
                result.append(map[target - numbers[i]] + 1)
                result.append(i + 1)
                return result
            map[numbers[i]] = i
        return result

A = [2, 7, 11, 15]
Sol = Solution()
print Sol.twoSum(A, 9)

