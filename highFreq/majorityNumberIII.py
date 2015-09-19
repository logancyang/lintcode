# majorityNumberIII: http://www.lintcode.com/en/problem/majority-number-iii/
# A number is the majority number in the list, it occurs more than N/k times. Find it.


class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # hash stores the most frequent k numbers
        counters = {}
        for number in nums:
            if number not in counters:
                counters[number] = 1
            else:
                counters[number] += 1

            if len(counters) >= k:
                # BUG: not removing the least frequent key
                # decrement by 1 like before, who got 0 count who's eliminated
                self.remove_key(counters)

        # corner case
        if len(counters) == 0:
            return -1
        # recompute counters
        for key in counters:
            counters[key] = 0
        for number in nums:
            if number in counters:
                counters[number] += 1
        # find the max value key
        result_number, max_count = 0, 0
        for key in counters:
            if counters[key] > max_count:
                max_count = counters[key]
                result_number = key
        return result_number

    def remove_key(self, counters):
        remove_list = []
        for key in counters:
            counters[key] -= 1
            if counters[key] == 0:
                remove_list.append(key)
        for key in remove_list:
            del counters[key]

A = [2,10,2,1,2]
Sol = Solution()
print Sol.majorityNumber(A, 2)