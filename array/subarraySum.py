# subarraySum: http://www.jiuzhang.com/solutions/subarray-sum/
# return ANY subarray start, end indices that sums to 0
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number. Summing to 0.
    """
    def subarraySum(self, nums):
        result = []
        # init the hashmap storing accumulated_sum: index
        # accumulated_sum = 0, index starting from -1
        map = {0: -1}
        
        sum = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            # accumulate to a sum and get an old_sum, meaning the accumulation
            # in the subarray starting from old_sum (that ind + 1) till now is 0
            if sum in map:
                result.append(map[sum]+1)
                result.append(i)
                return result
            map[sum] = i
        return result

nums = [3, 1, 2, -3, 4]
Sol = Solution()
print Sol.subarraySum(nums)