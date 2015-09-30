# subarraySumClosest: http://www.lintcode.com/en/problem/subarray-sum-closest/

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    # brute force O(n^3)
    def subarraySumClosestBrute(self, nums):
        result = [0, 0]
        if nums is None or len(nums) <= 1:
            return result
        min_dist = float("inf")
        # does allow [i, i], a single element as result
        for i in xrange(len(nums)):
            if abs(nums[i]) < min_dist:
                min_dist = abs(nums[i])
                result = [i, i]
        # this part is O(n^3), too slow
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                tmp_sum = sum(nums[i:j+1])
                distance = abs(tmp_sum)
                if distance < min_dist:
                    min_dist = distance
                    result = [i, j]
        return result

    def subarraySumClosest(self, nums):
        result = [0, 0]
        if nums is None or len(nums) <= 1:
            return result
        min_dist = float("inf")
        # does allow [i, i], a single element as result
        for i in xrange(len(nums)):
            if abs(nums[i]) < min_dist:
                min_dist = abs(nums[i])
                result = [i, i]
        # compute prefix_sum[i] = sum(nums[:i+1]), O(n)
        accumulator = 0
        pair_sum_ind = []
        for i in xrange(len(nums)):
            accumulator += nums[i]
            # accumulator is prefix_sum[i], i inclusive
            pair_sum_ind.append((accumulator, i))
        pair_sum_ind.sort(key=lambda tup: tup[0])
        min_diff = float("inf")
        for i in xrange(1, len(nums)):
            diff = abs(pair_sum_ind[i][0] - pair_sum_ind[i-1][0])
            if diff < min_diff:
                min_diff = diff
                result = [pair_sum_ind[i][1], pair_sum_ind[i-1][1]]
        result.sort()
        # since prefix_sum[j] - prefix_sum[i] refers to subarray sum i+1 to j
        # the smaller index in prefix_sum should + 1
        result[0] = result[0] + 1
        return result

A = [-3, 1, 1, -3, 5]
Sol = Solution()
print Sol.subarraySumClosest(A)