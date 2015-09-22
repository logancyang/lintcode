# maxSubarray: http://www.lintcode.com/en/problem/maximum-subarray/

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        # don't explicitly compute prefix_sum, it's O(n^2)
        # prefix_sum = [sum(nums[:i+1]) for i in xrange(len(nums))]
        result = []
        max_diff = float("-inf")
        # the min previous prefix_sum for a fixed end point
        accumulator, min_sum = 0, 0
        for i in xrange(len(nums)):
            accumulator += nums[i]
            max_diff = max(accumulator - min_sum, max_diff)
            result.append(max_diff)
            min_sum = min(min_sum, accumulator)
        # return max_diff
        return result

A = [1,2,1,4,1,-10,1,6,3]
Sol = Solution()
print Sol.maxSubArray(A)
