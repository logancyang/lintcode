# fourSum: http://www.lintcode.com/en/problem/4-sum/

class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        if numbers is None or len(numbers) < 4:
            return []
        numbers.sort()
        twoSums = {}
        result_set = set([])
        # enumerate all 1st two numbers
        # store their sum in dict
        for i in xrange(len(numbers)):
            for j in xrange(i+1, len(numbers)):
                twoSum = numbers[i] + numbers[j]
                if twoSum not in twoSums:
                    twoSums[twoSum] = [(i, j)]
                else:
                    twoSums[twoSum].append((i, j))
        # check last two numbers
        for i in xrange(len(numbers)):
            for j in xrange(i+1, len(numbers)):
                lastTwoSum = numbers[i] + numbers[j]
                firstTwoSum = target - lastTwoSum
                if firstTwoSum in twoSums:
                    for pair in twoSums[firstTwoSum]:
                        if pair[0] > j:
                            local = (numbers[i], numbers[j], numbers[pair[0]], numbers[pair[1]])
                            result_set.add(local)
        result = list(result_set)
        result = [list(sub_tuple) for sub_tuple in result]
        return result

A = [1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,0,0,-2,2,-5,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99]
target = 11
Sol = Solution()
print Sol.fourSum(A, target)