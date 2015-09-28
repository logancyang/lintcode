# partitionArray: http://www.lintcode.com/en/problem/partition-array/

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if nums is None or len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        pivot = k
        while start < end:
            while start <= end and nums[start] < pivot:
                start += 1
            while start <= end and nums[end] >= pivot:
                end -= 1
            if start <= end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
        # start is the point where it first >= pivot, we want start
        # end is the point it first becomes < pivot
        return start

A = [1, 8, 4, 3, 5]
Sol = Solution()
print Sol.partitionArray(A, 3)
print A


