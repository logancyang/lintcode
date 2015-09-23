# twoSum: http://www.lintcode.com/en/problem/2-sum/

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    # hashmap, O(n) space, O(n) time
    def twoSum(self, numbers, target):
        if numbers is None or len(numbers) == 0:
            return -1
        hashmap = {}
        for ind, num in enumerate(numbers):
            if num not in hashmap:
                hashmap[num] = ind + 1
        for ind, num in enumerate(numbers):
            if target - num in hashmap:
                result = [hashmap[target - num], ind + 1]
                result.sort()
                return result
        return -1

    # 2-pointers: need the list sorted. O(nlogn) time
    # if we want the two numbers, O(1) space; if indices, still O(n) space
    def twoSum2pointers(self, numbers, target):
        if numbers is None or len(numbers) == 0:
            return -1
        numbers_tup = [(ind, num) for ind, num in enumerate(numbers)]
        numbers_tup.sort(key=lambda (ind, num): num)
        start = 0
        end = len(numbers) - 1
        while start < end:
            if numbers_tup[start][1] + numbers_tup[end][1] == target:
                result = [numbers_tup[start][0] + 1, numbers_tup[end][0] + 1]
                result.sort()
                return result
            elif numbers_tup[start][1] + numbers_tup[end][1] > target:
                end -= 1
            else:
                start += 1
        return -1

A = [1,2,33,23,2423,33,23,1,7,6,8787,5,33,2,3,-23,-54,-67,100,400]
Sol = Solution()
print Sol.twoSum2pointers(A, 407)