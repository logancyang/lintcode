# majorityNumber: http://www.lintcode.com/en/problem/majority-number/
# find the majority number. it occurs more than N/2 times
# cannot use hash histogram, use O(1) space, O(n) time

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        count = 0; candidate = -1
        for number in nums:
            if count == 0:
                candidate = number
                count = 1
            elif number == candidate:
                count += 1
            else:
                count -= 1
        return candidate

A = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3]
Sol = Solution()
print Sol.majorityNumber(A)