# maxSubarrayIII: http://www.lintcode.com/en/problem/maximum-subarray-iii/
# DP

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        if nums is None or len(nums) < k:
            return 0
        len_nums = len(nums)
        # k partitions of array with length len_nums
        # BUG!! NEVER INITIALIZE 2D ARRAY LIKE THIS!! EACH SUBLIST POINTS TO THE SAME OBJECT!!
        # globalMax = [[0] * (len_nums + 1)] * (k + 1)
        globalMax = [[0 for j in xrange(len_nums+1)] for i in xrange(k+1)]
        # print globalMax
        for i in xrange(1, k+1):
            localMax = float("-inf")
            # array with length < i cannot be partitioned
            for j in xrange(i-1, len_nums):
                # print localMax, globalMax[i-1][j], nums[j]
                localMax = max(localMax, globalMax[i-1][j]) + nums[j]
                # print localMax
                if j == i - 1:
                    globalMax[i][j+1] = localMax
                else:
                    globalMax[i][j+1] = max(globalMax[i][j], localMax)
        return globalMax[k][len_nums]

A = [-1,4,-2,3,-2,3]
k = 2
Sol = Solution()
print Sol.maxSubArray(A, k)