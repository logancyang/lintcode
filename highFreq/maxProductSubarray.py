# maxProductSubarray: http://www.lintcode.com/en/problem/maximum-product-subarray/

class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        minlist = [0] * len(nums)
        maxlist = [0] * len(nums)
        minlist[0] = nums[0]
        maxlist[0] = nums[0]
        result = nums[0]
        for i in xrange(1, len(nums)):
            # local max product ending at i
            maxlist[i] = max(nums[i], nums[i] * maxlist[i-1], nums[i] * minlist[i-1])
            # local min product ending at i
            minlist[i] = min(nums[i], nums[i] * maxlist[i-1], nums[i] * minlist[i-1])
            result = max(result, maxlist[i])
        return result

A = [2, 3, -1, 4]
Sol = Solution()
print Sol.maxProduct(A)