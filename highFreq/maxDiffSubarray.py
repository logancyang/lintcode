# maxDiffSubarrays: http://www.lintcode.com/en/problem/maximum-subarray-difference/

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        left_small, right_small = self.scanSubarray(nums, "small")
        left_big, right_big = self.scanSubarray(nums, "big")
        max_diff = 0
        # BUG: range len-1, left[i] with right[i+1]
        for i in xrange(len(nums)-1):
            max_diff = max(abs(left_small[i] - right_big[i+1]), max_diff)
            max_diff = max(abs(left_big[i] - right_small[i+1]), max_diff)
        return max_diff

    def scanSubarray(self, nums, big_or_small):
        if big_or_small == "small":
            nums_new = [-item for item in nums]
        elif big_or_small == "big":
            nums_new = nums
        left_new = [0] * len(nums)
        right_new = [0] * len(nums)
        accumulator = 0
        minSum = 0
        max_diff = float("-inf")
        # left_new
        for i in xrange(len(nums)):
            accumulator += nums_new[i]
            max_diff = max(max_diff, accumulator - minSum)
            minSum = min(minSum, accumulator)
            if big_or_small == "small":
                left_new[i] = -max_diff
            else:
                left_new[i] = max_diff
        # right_new
        accumulator = 0
        minSum = 0
        max_diff = float("-inf")
        for i in xrange(len(nums)-1, -1, -1):
            accumulator += nums_new[i]
            max_diff = max(max_diff, accumulator - minSum)
            minSum = min(minSum, accumulator)
            if big_or_small == "small":
                right_new[i] = -max_diff
            else:
                right_new[i] = max_diff
        return left_new, right_new

A = [-4, -5]
Sol = Solution()
print Sol.maxDiffSubArrays(A)

