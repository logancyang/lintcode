# sortColors: http://www.lintcode.com/en/problem/sort-colors/
# sort "red" (0), "white" (1), "blue" (2) in this order

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    # 2-pointers: check colors in order
    # e.g. for red (0), check red or not red, put red in front
    # next pass, start from the 1st non-red (white, 1), put white in front...
    def sortColors(self, nums):
        start = 0
        pivot = 0
        start = self.partitionArray(nums, start, 0)
        self.partitionArray(nums, start, 1)
        return nums

    def partitionArray(self, nums, start, pivot):
        end = len(nums) - 1
        while start < end:
            while start <= end and nums[start] == pivot:
                start += 1
            while start <= end and nums[end] != pivot:
                end -= 1
            if start < end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
        return start

A = [1, 0, 1, 2]
Sol = Solution()
print Sol.sortColors(A)

