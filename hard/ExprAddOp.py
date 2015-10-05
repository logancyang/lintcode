__author__ = 'loganyang'

# ExprAddOp: https://leetcode.com/problems/expression-add-operators/
# "123", 6 --> ["1+2+3", "1*2*3"]
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
# D&C: dfs(left_num), left_num, "+" or "-" or "*", right_num --> target


class Solution(object):

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # add to global result when eval(path) == target
        self.result = []
        if num is None or len(num) == 0:
            return self.result
        # left = num[:ind+1], right = num[ind+1:]
        ind = 0
        eva = 0
        mult = 0
        # num, target, path, ind, eva, mult
        self.dfs(num, target, "", ind, eva, mult)
        return self.result

    def dfs(self, num, target, path, ind, eva, mult):
        # base
        if ind == len(num):
            if eva == target:
                self.result.append(path)
            return
        # non-base
        for i in xrange(ind, len(num)):
            if i != ind and num[ind] == '0':
                break
            left = num[ind:i+1]
            leftVal = int(left)
            if ind == 0:
                self.dfs(num, target, path + left, i+1, leftVal, leftVal)
            else:
                # +
                new_path = path + '+' + left
                self.dfs(num, target, new_path, i+1, eva + leftVal, leftVal)
                # -
                new_path = path + '-' + left
                self.dfs(num, target, new_path, i+1, eva - leftVal, -leftVal)
                # *
                new_path = path + '*' + left
                self.dfs(num, target, new_path, i+1, eva - mult + mult * leftVal, mult * leftVal)
        return

A = '123'
target = 6
Sol = Solution()
print Sol.addOperators(A, target)