# threeSumClosest: http://www.lintcode.com/en/problem/3-sum-closest/
# 2-pointers meet scan


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        result = []
        if numbers is None or len(numbers) < 3:
            return result

        numbers.sort()
        closest_dist = float("inf")

        for i in xrange(len(numbers) - 2):
            # skip duplicates
            if i != 0 and numbers[i] == numbers[i-1]:
                continue
            left = i + 1
            right = len(numbers) - 1
            while left < right:
                sum = numbers[i] + numbers[left] + numbers[right]
                dist = sum - target
                if sum == target:
                    return sum
                # different than 3-Sum, do not update pointers here
                # dist = sum - target < 0 meaning we need bigger sum
                elif dist < 0:
                    left += 1
                else:
                    right -= 1
                if abs(dist) < closest_dist:
                    closest_dist = abs(dist)
                    result = sum
        return result

A = [2, 7, 11, 15]
Sol = Solution()
print Sol.threeSumClosest(A, 3)