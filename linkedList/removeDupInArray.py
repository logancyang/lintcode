# removeDupInArray: in-place, return the new length (doesn't matter what's beyond the new length)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # len = 0, 1
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        # len > 1
        current = nums[0]
        end = 1
        for cursor in xrange(1, len(nums)):
            if nums[cursor] == current:
                continue
            current = nums[cursor]
            nums[cursor], nums[end] = nums[end], nums[cursor]
            # nums[end] now = previous nums[cursor]
            # current = nums[end]
            end += 1
        return end

A = [0, 1, 2, 3, 4, 5]
i = 0
j = 2
print A, A[j]
A[i], A[j] = A[j], A[i]
print A, A[j]