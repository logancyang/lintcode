# majorityNumberII: http://www.lintcode.com/en/problem/majority-number-ii/

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        candidate1, candidate2 = -1, -1
        count1, count2 = 0, 0
        for number in nums:
            # BUG: check num == candidate first, then check count == 0. Or it's wrong
            if number == candidate1:
                count1 += 1
            elif number == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = number
                count1 = 1
            elif count2 == 0:
                candidate2 = number
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # count again to make sure
        count1 = count2 = 0
        for number in nums:
            if number == candidate1:
                count1 += 1
            elif number == candidate2:
                count2 += 1

        return candidate1 if count1 > count2 else candidate2
