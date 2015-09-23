# minSubarray: http://www.lintcode.com/en/problem/minimum-subarray/

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        new_nums = [-item for item in nums]
        accumulator = 0
        minSum = 0
        result = []
        max_diff = float("-inf")
        for i in xrange(len(new_nums)):
            accumulator += new_nums[i]
            max_diff = max(max_diff, accumulator - minSum)
            # result.append(max_diff)
            minSum = min(minSum, accumulator)
        return -max_diff
        # return result

A = [1,-1,-2,1]
Sol = Solution()
print Sol.minSubArray(A)