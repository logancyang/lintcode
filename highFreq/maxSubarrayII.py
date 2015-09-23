# maxSubarrayII: http://www.lintcode.com/en/problem/maximum-subarray-ii/
# find max_diff in accumulator <==> find max subarray sum

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        left = [0] * len(nums)
        right = [0] * len(nums)
        # left, left[i] := max_subarray_sum(nums[:i])
        accumulator = 0
        minSum = 0
        max_diff = float("-inf")
        for i in xrange(len(nums)):
            accumulator += nums[i]
            max_diff = max(max_diff, accumulator - minSum)
            minSum = min(minSum, accumulator)
            left[i] = max_diff

        # right, right[i] := max_subarray_sum(nums[i+1:])
        accumulator = 0
        minSum = 0
        max_diff = float("-inf")
        for i in xrange(len(nums)-1, -1, -1):
            accumulator += nums[i]
            max_diff = max(max_diff, accumulator - minSum)
            minSum = min(minSum, accumulator)
            right[i] = max_diff
        # BUG: range len-1, left[i] with right[i+1]
        max_diff = max([left[i] + right[i+1] for i in xrange(len(nums)-1)])
        return left, right
        # return max_diff

# A = [1, 3, -1, 2, -1, 2]
A = [-1,-2,-3,-100,-1,-50]
Sol = Solution()
print Sol.maxTwoSubArrays(A)