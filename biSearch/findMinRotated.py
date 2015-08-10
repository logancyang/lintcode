class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if num is None or len(num) == 0:
            return
        start = 0
        end = len(num) - 1
        while start + 1 < end:
            mid = (start + end)/2
            # do not compare with num[start]
            # because if num is not rotated, namely [end] is max
            # and [start] is min, this leads to an error
            if num[mid] > num[end]:
                start = mid
            if num[mid] <= num[end]:
                end = mid

        return min(num[start], num[end])

A = [1, 2, 3]
Sol = Solution()
print Sol.findMin(A)